from abc import ABC, abstractmethod

# 추상 클래스를 만들기 위해선 ABC를 임포트해 상속받아야 한다
class Vehicle(ABC):

    # 데코레이터를 활용해 추상 메소드 만들기
    @abstractmethod
    def start(self):
        """주행 시작"""
        print("자전거는 인도로.")
        pass

    @property
    @abstractmethod
    def speed(self):
        """변수 _speed(교통 수단의 속도)에 대한 추상 getter 메소드"""
        pass

    def stop(self):
        """일반 메소드 stop: 교통 수단의 속도를 0으로 바꾼다"""
        self.speed = 0
        

class Bicycle(Vehicle):
    max_speed = 15  # 자전거의 최대 속도
    
    def __init__(self, speed):
        self._speed = speed

    # 데코레이터를 활용하여 _speed 변수 캡슐화
    @property
    def speed(self):
        return self._speed
    
    # 얘도 마찬가지
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= Bicycle.max_speed else 0

    def start(self):
        # super()을 이용한, 추상 메소드의 기존 내용을 포함한 오버라이딩
        super().start()
        print("자전거 페달 돌리기 시작합니다.")
        self.speed = Bicycle.max_speed / 3    
        
    def __str__(self):
        return "이 자전거는 현재 {}km/h로 주행 중입니다.".format(self.speed)
        
        
class NormalCar(Vehicle):
    
    def __init__(self, speed, max_speed):
        self._speed = 0
        self.max_speed = max_speed
        
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0
    
    def start(self):
        print("일반 자동차 시동겁니다.")
        self.speed = self.max_speed / 2    

    def __str__(self):
        return "이 일반 자동차는 현재 {}km/h로 주행 중입니다.".format(self.speed)

    
class SportsCar(Vehicle):
    
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed
        
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0
               
    def start(self):
        print("스포츠카 시동겁니다.")
        self.speed = self.max_speed
             
    def __str__(self):
        return "이 스포츠카는 현재 {}km/h로 주행 중입니다.".format(self.speed)


class DrivingSimulator:
    def __init__(self):
        """교통 수단 인스턴스들을 담을 리스트를 변수로 갖는다"""
        self.simulator = []

    def add_vehicle(self, new_vehicle):
        """교통 수단 인스턴스들만 시뮬레이터에 추가"""
        # isinstance()함수를 활용
        if isinstance(new_vehicle, Vehicle):
            self.simulator.append(new_vehicle)
        else:
            print("{}은 교통 수단이 아니기 때문에 추가할 수 없습니다.".format(new_vehicle))

    def start_all_vehicles(self):
        """모든 교통 수단 주행 시작"""
        print("모든 교통 수단을 주행 시작시킵니다!\n")
        # : Vehicle은 type hinting 으로 자료형을 표시해 주는 것
        for vehicle: Vehicle in self.simulator:
            vehicle.start()

    def stop_all_vehicles(self):
        """모든 교통 수단 주행 정지"""
        print("\n모든 교통 수단을 주행 정지시킵니다!\n")
        for vehicle in self.simulator:
            vehicle.stop()

    def __str__(self) -> str:
        """갖고 있는 교통 수단들의 현재 속도를 문자열로 리턴"""
        string = ""
        for vehicle in self.simulator:
            string += str(vehicle) + "\n"
        return string

# 자전거 인스턴스
bicycle = Bicycle(0)

# 일반 자동차 인스턴스들
car_1 = NormalCar(0, 100)
car_2 = NormalCar(0, 120)

# 스포츠카 인스턴스들
sports_car_1 = SportsCar(0, 200)
sports_car_2 = SportsCar(0, 190)


# 주행 시뮬레이터 인스턴스
driving_simulator = DrivingSimulator()

# 교통 수단 인스턴스들을 주행 시뮬레이터에 추가한다
driving_simulator.add_vehicle(bicycle)
driving_simulator.add_vehicle(car_1)
driving_simulator.add_vehicle(car_2)
driving_simulator.add_vehicle(sports_car_1)
driving_simulator.add_vehicle(sports_car_2)
driving_simulator.add_vehicle(1)

# 시뮬레이터 내 모든 인스턴스들을 주행 시작시킨다
driving_simulator.start_all_vehicles()
print(driving_simulator)

# 시뮬레이터 내 모든 인스턴스들을 주행 정지시킨다
driving_simulator.stop_all_vehicles()
print(driving_simulator)

# 클래스 내에 문서화된 주석들만 모아 볼 수 있는 함수
help(Vehicle)

# 부모 클래스들을 상속 순서로 볼 수 있게 해주는 메소드
print(NormalCar.mro())