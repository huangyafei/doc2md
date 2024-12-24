from fastapi import APIRouter, UploadFile, HTTPException, Depends
from app.services.converter import MarkdownConverter
from app.api.auth import verify_api_key
from typing import Optional
import io

router = APIRouter()

@router.post("/convert")
async def convert_to_markdown(
    file: UploadFile,
    llm_enabled: Optional[bool] = False,
    api_key: str = Depends(verify_api_key)
):
    """
    将上传的文件转换为 Markdown 格式
    
    Args:
        file: 上传的文件
        llm_enabled: 是否启用 LLM 功能(用于图像描述等)
    
    Returns:
        dict: 包含转换后的 markdown 内容
    """
    try:
        # 读取文件内容
        content = await file.read()
        file_obj = io.BytesIO(content)
        
        # 获取文件扩展名
        filename = file.filename
        file_extension = f".{filename.split('.')[-1]}" if "." in filename else ""
        
        # 转换文件
        converter = MarkdownConverter()
        result = converter.convert_stream(
            file_obj,
            file_extension=file_extension,
            filename=filename,
            llm_enabled=llm_enabled
        )
        
        return {
            "markdown": result.text_content,
            "filename": filename
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 