import os
import time

class FileMonitor:

    def __init__(self, folder_path, roboflow_client):
        self.folder_path = folder_path
        self.roboflow_client = roboflow_client
        self.existing_files = set(os.listdir(self.folder_path))

    def monitor_folder(self):
        while True:
            current_files = set(os.listdir(self.folder_path))
            new_files = current_files - self.existing_files

            for new_file in new_files:
                new_file_path = os.path.join(self.folder_path, new_file)
                print(f"새 이미지가 감지되었습니다: {new_file_path}")
                result = self.roboflow_client.infer_image(new_file_path, model_id="kids_adult/3")
                print(f"result : {result}") # Json 결과 출력
                class_value = self.roboflow_client.get_class_from_result(result)
                if class_value == "kids": # Input Image = Kids
                    #print("kids")   # Console Log(Debug)
                    return True
                else: # Input Image = Adults
                    #print("Adult")   # Console Log(Debug)
                    return False 

            self.existing_files = current_files
            time.sleep(1)

if __name__ == "__main__":
    from roboflow import RoboflowClient

    
    folder_path = "TestImage"
    roboflow_client = RoboflowClient(api_url="https://detect.roboflow.com", api_key="")
    
    file_monitor = FileMonitor(folder_path, roboflow_client)
    image_TnF = file_monitor.monitor_folder()

    #if문을 사용한 릴레이 모듈 컨트롤 코드 작성

    #ex)예시
    if(image_TnF == True) : print("어린아이")
    else : print("성인")
