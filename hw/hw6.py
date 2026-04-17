class User:
    def __init__(self,name,role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            func(user)
        else:
            print("У вас нет доступа")
    return wrapper



@is_admin
def delete_video(user):
    print("Видео удалено")



admin = User("Kalys","admin")
user = User("Chuke","user")

delete_video(admin)
delete_video(user)



import time

def timer(func):
    def wrap():
        start = time.time()

        func()

        end = time.time()
        print(f" Время выполнения:", end - start)
    return wrap


@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")

download_video()





















