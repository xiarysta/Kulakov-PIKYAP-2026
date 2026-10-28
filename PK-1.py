class File:

    def __init__(self, id: int, name: str, size: int, directory_id: int):
        self.id = id
        self.name = name
        self.size = size
        self.directory_id = directory_id

class Directory:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class FileDirectory:

    def __init__(self, file_id: int, directory_id: int):
        self.file_id = file_id
        self.directory_id = directory_id


directories: list[Directory] = [
    Directory(1, "Каталог документов"),
    Directory(2, "Каталог изображений"),
    Directory(3, "Архив"),
]

files: list[File] = [
    File(1, "Анкета.docx", 120, 1),
    File(2, "Отчет.pdf", 251, 1),
    File(3, "Аватар.png", 800, 2),
    File(4, "Фото.jpg", 1500, 2),
    File(5, "Резервная_копия.zip", 5000, 3),
]

files_directories: list[FileDirectory] = [
    FileDirectory(1, 1),
    FileDirectory(1, 3),
    FileDirectory(3, 2),
    FileDirectory(3, 3),
    FileDirectory(5, 3),
]

def main() -> None:

    print("Задание 1")

    for directory in directories:

        if ("каталог" in directory.name.lower()):
            print(f"{directory.name}:")

            for file in files:
                if (file.directory_id == directory.id):
                    print(f"    {file.name}")

    print("\nЗадание 2")

    averages: list[tuple[str, float]] = []
    
    for directory in directories:
        sizes: list[int] = [
            file.size for file in files
            if file.directory_id == directory.id
        ]

        if sizes:
            average = round(sum(sizes) / len(sizes), 2)
            averages.append((directory.name, average))

    averages.sort(key=lambda item: item[1])

    for name, value in averages:
        print(f"{name}: {value:.2f} КБ")

    print("\nЗадание 3")

    for file in files:

        if (file.name.lower().startswith("а")):
            print(f"{file.name}:")

            for link in files_directories:
                if (link.file_id == file.id):

                    for directory in directories:
                        if (directory.id == link.directory_id):
                            print(f"    {directory.name}")


if __name__ == "__main__":
    main()
