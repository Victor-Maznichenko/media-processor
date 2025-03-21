from media_processor import image_utils, audio_video_utils, pdf_utils, graphics_utils

PATH_AUDIO = 'assets/sounds/'
PATH_PDF = 'assets/mergePDF/'
PATH_BLUR = 'assets/blurImage/'
PATH_WATERMARK = 'assets/watermark/'

def main():
    # Пример: применение размытия к изображению
    image_utils.apply_blur_filter(f"{PATH_BLUR}input.jpg", f"{PATH_BLUR}blurred.jpg", radius=5)

    # Пример: конвертация аудио файла

    # Пример: объединение двух PDF файлов
    pdf_files = [f"{PATH_PDF}doc1.pdf", f"{PATH_PDF}doc2.pdf"]
    pdf_utils.merge_pdfs(pdf_files, f"{PATH_PDF}merged.pdf")

    # Пример: добавление водяного знака
    graphics_utils.add_watermark(f"{PATH_WATERMARK}photo.jpg", f"{PATH_WATERMARK}watermark.png",
                                 f"{PATH_WATERMARK}watermarked_photo.jpg", position=(20, 20))

    # Пример: Конвертация аудио из одного формата в другой
    audio_video_utils.convert_audio(f"{PATH_AUDIO}input.wav", f"{PATH_AUDIO}output.mp3", f="mp3")
    print("Конвертация завершена: input.wav -> output.mp3")

    # Пример: Изменение громкости аудиофайла (увеличение на 5 дБ)
    audio_video_utils.adjust_volume(f"{PATH_AUDIO}input.wav", "output_louder.mp3", db_change=5, f="mp3")
    print("Громкость увеличена на 5 дБ: input.wav -> output_louder.mp3")

    # Пример: Нормализация громкости аудиофайла
    audio_video_utils.normalize_audio(f"{PATH_AUDIO}input.wav", "output_normalized.mp3", f="mp3")
    print("Нормализация завершена: input.wav -> output_normalized.mp3")

    # Пример: Объединение нескольких аудиофайлов в один
    file_names = ["input1.wav", "input2.wav", "input3.wav"]
    audio_video_utils.merge_audio_files(f"{PATH_AUDIO}merges/", file_names, f"{PATH_AUDIO}merges/merged_output.mp3", f="mp3")
    print("Файлы объединены в merged_output.mp3")

if __name__ == '__main__':
    main()
