from markitdown import MarkItDown
from typing import Optional
import io

class MarkdownConverter:
    def __init__(self):
        self._converter = MarkItDown()
    
    def convert_stream(
        self,
        file_obj: io.BytesIO,
        file_extension: str = "",
        filename: Optional[str] = None,
        llm_enabled: bool = False
    ):
        """
        转换文件流为 Markdown
        
        Args:
            file_obj: 文件对象
            file_extension: 文件扩展名
            filename: 文件名
            llm_enabled: 是否启用 LLM
        """
        if llm_enabled:
            # 如果需要 LLM 功能,需要配置 OpenAI client
            from openai import OpenAI
            client = OpenAI()
            self._converter = MarkItDown(
                llm_client=client,
                llm_model="gpt-4-vision-preview"
            )
            
        return self._converter.convert_stream(
            file_obj,
            file_extension=file_extension,
            url=filename
        ) 