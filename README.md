# Media Processor

A Python package that provides utilities for processing media files.

## 💡Features
- **Image Utilities:** Apply filters and effects to images.
- **Audio/Video Utilities:** Convert formats, adjust volume, normalize audio, and merge files.
- **PDF Utilities:** Merge PDF files and extract graphics.
- **Graphics Utilities:** Add watermarks and create collages.

## 🔧Installation
Install via pip:

```bash
pip install media_processor
```

## 🧙‍♀️Usage
Applying a Blur Filter to an Image
``` python
image_utils.apply_blur_filter(f"{PATH_BLUR}input.jpg", f"{PATH_BLUR}blurred.jpg", radius=5)
```

Converting an Audio File
``` python
audio_video_utils.convert_audio(f"{PATH_AUDIO}input.wav", f"{PATH_AUDIO}output.mp3", f="mp3")
```

Merging Two PDF Files
``` python
pdf_files = [f"{PATH_PDF}doc1.pdf", f"{PATH_PDF}doc2.pdf"]
pdf_utils.merge_pdfs(pdf_files, f"{PATH_PDF}merged.pdf")
```

Adding a Watermark to an Image
``` python
graphics_utils.add_watermark(f"{PATH_WATERMARK}photo.jpg", f"{PATH_WATERMARK}watermark.png",
                             f"{PATH_WATERMARK}watermarked_photo.jpg", position=(20, 20))
```

