class InvalidInput(Exception):
    """Исключение для неправильного формата ввода."""
    pass

class BadTriangle(Exception):
    """Исключение для случая, когда введенные координаты не формируют треугольник."""
    pass

def triangleSquare(inStr):
    try:
        # Преобразование строки во множество координат
        coords = eval(inStr)
        
        # Проверка на правильность формата
        if not (isinstance(coords, tuple) and len(coords) == 3 and 
                all(isinstance(point, tuple) and len(point) == 2 for point in coords)):
            raise InvalidInput
        
        # Извлечение координат
        (x1, y1), (x2, y2), (x3, y3) = coords
        
        # Проверка на корректность координат
        if (x1, y1) == (x2, y2) or (x2, y2) == (x3, y3) or (x1, y1) == (x3, y3):
            raise BadTriangle
        
        # Вычисление площади треугольника по формуле Герона
        area = abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)
        
        # Проверка на нулевую площадь
        if area == 0:
            raise BadTriangle
        
        return round(area, 2)
    
    except Exception:
        raise InvalidInput

if __name__ == "__main__":
    while True:
        user_input = input("Введите координаты вершин треугольника в формате ((x1, y1), (x2, y2), (x3, y3)): ")
        
        try:
            area = triangleSquare(user_input)
            print(f"Площадь треугольника: {area}")
            break  # Выход из цикла, если ввод корректен
        except InvalidInput:
            print("Invalid input")
        except BadTriangle:
            print("Not a triangle")

# Тесты
def test_triangleSquare():
    # Тест на неправильный формат
    try:
        triangleSquare("((1, 2), (3, 4), (5))")  # Неправильный формат
    except InvalidInput:
        print("Test passed: Invalid input format caught.")

    # Тест на не-треугольник
    try:
        triangleSquare("((1, 1), (1, 1), (1, 1))")  # Все точки совпадают
    except BadTriangle:
        print("Test passed: Not a triangle caught.")

    try:
        triangleSquare("((0, 0), (0, 0), (1, 1))")  # Две точки совпадают
    except BadTriangle:
        print("Test passed: Not a triangle caught.")

    try:
        triangleSquare("((0, 0), (1, 1), (2, 2))")  # Все точки на одной прямой
    except BadTriangle:
        print("Test passed: Not a triangle caught.")

test_triangleSquare()
