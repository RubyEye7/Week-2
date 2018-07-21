class Polygon:

    def __init__(self):
        self.points = []

    def distance_formula(self, x1, y1, x2, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    def addPoint(self, x, y):
        self.points.append([x, y])

    def perimeter(self):
        answer = 0
        self.perimeter = 0.0
        for i in range(len(self.points)-1):
            x1 = self.points[i][0]
            y1 = self.points[i][1]
            x2 = self.points[i+1][0]
            y2 = self.points[i+1][1]
            answer = answer + ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        answer = answer + self.distance_formula(self.points[0][0], self.points[0][1], self.points[len(self.points)-1][0], self.points[len(self.points)-1][1])
        return answer

    def area(self):
        points = self.points
        x = 0
        answer = 0
        points.append(points[0])
        while x < len(points) - 1:
            answer1 = points[x][0]*points[x+1][1] - points[x+1][0] * points[x][1]
            x += 1
            answer += answer1
        return abs(answer) / 2

p = Polygon()
p.addPoint(0,0)
p.addPoint(1,1)
p.addPoint(0,1)
print (p.perimeter())
print (p.area())
