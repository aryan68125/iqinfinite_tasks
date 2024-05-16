import os
import pkgutil

class ListPackageFiles:
    def __init__(self,package_name):
        self.__package_name = package_name
    
    def list_package_files(self):
        package_name = self.__package_name 
        package_path = os.path.dirname(pkgutil.get_loader(package_name).path)
        package_files = []
        for root, dirs, files in os.walk(package_path):
            for file in files:
                if file.endswith('.py'):
                    package_files.append(os.path.relpath(os.path.join(root, file), package_path))
        return package_files

# if __name__ == "__main__":
#     package_name = input("Enter your package name:")  # Replace "your_package_name" with your actual package name
#     files = list_package_files(package_name)
#     print("Files in package '{}':".format(package_name))
#     for file in files:
        print("-", file)