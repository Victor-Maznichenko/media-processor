from pydub import AudioSegment, effects

def convert_audio(input_path: str, output_path: str, f: str = 'mp3') -> None:
    """
    Конвертирует аудиофайл в указанный формат.

    :param input_path: Путь к исходному аудиофайлу.
    :param output_path: Путь для сохранения конвертированного файла.
    :param f: Целевой аудиоформат (например, 'mp3', 'wav').
    """
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format=f)

def adjust_volume(input_path: str, output_path: str, db_change: float, f: str = 'mp3') -> None:
    """
    Изменяет громкость аудиофайла.

    :param input_path: Путь к исходному аудиофайлу.
    :param output_path: Путь для сохранения файла с изменённой громкостью.
    :param db_change: Изменение громкости в децибелах (положительное значение для увеличения, отрицательное для уменьшения).
    :param f: Целевой аудиоформат.
    """
    audio = AudioSegment.from_file(input_path)
    # Изменение громкости: прибавляем заданное значение в децибелах
    modified = audio + db_change
    modified.export(output_path, format=f)

def normalize_audio(input_path: str, output_path: str, f: str = 'mp3') -> None:
    """
    Нормализует громкость аудиофайла.

    :param input_path: Путь к исходному аудиофайлу.
    :param output_path: Путь для сохранения нормализованного файла.
    :param f: Целевой аудиоформат.
    """
    audio = AudioSegment.from_file(input_path)
    normalized = effects.normalize(audio)
    normalized.export(output_path, format=f)

def merge_audio_files(files_path: str, file_names: list, output_path: str, f: str = 'mp3') -> None:
    """
    Объединяет несколько аудиофайлов в один.

    :param file_names:
    :param files_path:
    :param output_path: Путь для сохранения объединённого файла.
    :param f: Целевой аудиоформат.
    """
    merged_audio = AudioSegment.empty()
    for file_name in file_names:
        audio = AudioSegment.from_file(files_path + file_name)
        merged_audio += audio
    merged_audio.export(output_path, format=f)
