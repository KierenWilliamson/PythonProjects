# Name: Kieren Williamson
# Class: Comp 163-001
# Date: April 23, 2023,
# Description: Program that allows the user to enter grades and weights for their course. The user can test each method
# of the CourseCategories and CourseGrades class. The data entered by the user also remains persistent by writing and
# reading text files.

import copy


class CourseCategories:
    FILENAME = 'CourseCategories.txt'
    categories = ['Homework', 'Labs', 'Assessments', 'Assignments', 'Midterm', 'Final']
    _weights = dict()

# constructor
    def __init__(self):
        self._weights = dict()
        try:
            self.read_weights()
        except FileNotFoundError:
            self.set_weights()
            self.write_weights()
        except Exception:
            print('Unknown Error')

# get / set
    def get_weights(self, category):
        return int(self._weights[category]) / 100

# updates the dictionary holding the categories and their corresponding weights
    def set_weights(self):
        self._weights.clear()
        for cat in self.categories:
            wgt = int(input('Enter weight for ' + cat + ': '))
            self._weights.update({cat: wgt})

# methods for CourseCategories class
# updates the weights dictionary by reading the text file created by write_weights
    def read_weights(self):
        fp = open(self.FILENAME, 'r')
        lines = fp.readlines()
        for line in lines:
            item = line.split(',')
            self._weights.update({item[0]: int(item[1])})
        fp.close()

# creates a text file and writes in the keys, value pairs from the weights dictionary
    def write_weights(self):
        fp = open(self.FILENAME, 'w')
        for key, value in self._weights.items():
            fp.write(key + ',' + str(value) + '\n')
        fp.close()

# edits the weights dictionary
    def edit(self, category, weight):
        self._weights.update({category: weight})
        self.write_weights()

# prints the grading categories and their corresponding weights
    def display(self):
        value_display = 1
        for category, weight in self._weights.items():
            print(str(value_display) + ') ' + category + ': ' + str(weight) + '%')
            value_display += 1
        return value_display

    def __str__(self):
        value_display = 1
        value = ''
        for category, weight in self._weights.items():
            value += str(value_display) + ') ' + category + '\n'
            value_display += 1
        return value


class CourseGrades:
    FILENAME = 'CourseGrades.txt'
    _gradelist = list()
    _grades = dict()

# In the constructor, myCat is initialized as a CourseCategories object
    def __init__(self):
        self.myCat = CourseCategories()
        self.categories = self.myCat.categories
        try:
            self.read_grades()
        except FileNotFoundError:
            self.set_grades()
            self.write_grades()
        except Exception:
            print('Unknown Error')

# get / set grades
    def set_grades(self):
        for category in self.categories:
            count = int(input(f'How many grades would you like to enter for the category "{category}"?: '))
            for g in range(count):
                grd = float(input(f'Enter the grades for the category "{category}": '))
                self._gradelist.append(grd)
            self._grades.update({category: copy.deepcopy(self._gradelist)})
            self._gradelist.clear()

    def get_grades(self, category):
        grd_list = self._grades[category]
        output = ''
        for g in grd_list:
            output += str(g) + ' '
        return output

# methods for the class CourseGrades
    def write_grades(self):
        fp = open(self.FILENAME, 'w')
        for key, values in self._grades.items():
            fp.write(key)
            for value in values:
                fp.write(f',{value}')
            fp.write('\n')
        fp.close()

    def read_grades(self):
        fp = open(self.FILENAME, 'r')
        lines = fp.readlines()
        for line in lines:
            line = line[:-1]
            item = line.split(',')
            self._grades.update({item[0]: item[1:]})
        fp.close()

    def edit_grades(self, category, grades):
        self._grades.update({category: grades})

# outputs the categories and their respective grades
    def display_grades(self):
        value_display = 1
        for categories, grades in self._grades.items():
            print(f'\n{str(value_display)}) {categories}')
            for grade in grades:
                print(f'{grade}', end=' ')
            value_display += 1
        print('\n')

    def calc_grade(self):
        final_grade = 0
        grade_sum = 0
        for category, grades in self._grades.items():
            for grade in grades:
                grade_sum += float(grade)
            avg = grade_sum / len(grades)
            grade_sum = 0
            wgt_avg = avg * self.myCat.get_weights(category)
            final_grade += wgt_avg
        print(f'You\'re final grade is: {final_grade:.2f}')

    def __str__(self):
        value_display = 1
        value = ''
        for category, grades in self._grades.items():
            value += str(value_display) + ') ' + category + '\n'
            value_display += 1
        return value


def main_menu():
    print(f'{"Main Menu":-^50}\n')
    print('1) Course Categories')
    print('2) Course Grades')
    print('3) Calculate Final Grade')
    print('4) Quit')
    print(f'-'*50)


def category_menu():
    print(f'{"Course Category Menu":-^50}\n')
    print('1) Display grade categories')
    print('2) Edit grade categories')
    print('3) Read grade categories')
    print('4) Write grade categories')
    print('5) Get grade categories')
    print('6) Set grade categories')
    print('7) Quit')
    print(f'-'*50)


def grade_menu():
    print(f'{"Course Grades Menu":-^50}\n')
    print('1) Display grades')
    print('2) Edit grades')
    print('3) Read Grades')
    print('4) Write Grades')
    print('5) Get Grades')
    print('6) Set Grades')
    print('7) Quit')
    print(f'-' * 50)


validMainMenu = (1, 2, 3, 4)
validCatMenu = (1, 2, 3, 4, 5, 6, 7)
validGradeMenu = (1, 2, 3, 4, 5, 6, 7)


if __name__ == '__main__':
    while True:
        myCourse = CourseCategories()
        myGrades = CourseGrades()
        main_menu()
        menuChoice = int(input('Menu Selection: '))
        print()
        if menuChoice not in validMainMenu:
            print('Invalid Menu Selection. Please try again.\n')
        elif menuChoice == 4:
            break
    # Course Categories menu options
        elif menuChoice == 1:
            category_menu()
            subMenuChoice = int(input('Menu Selection: '))
            print()
        # Allows the user to quit the menu
            if subMenuChoice not in validCatMenu:
                print('Invalid Menu Selection')
            elif subMenuChoice == 7:
                break
        # Displays the grading categories and their respective weights
            elif subMenuChoice == 1:
                myCourse.display()
        # Allows the user to edit the weights for the grading categories
            elif subMenuChoice == 2:
                myCourse.display()
                catChoice = int(input('Enter the number of the category you want to edit: '))
                catChoice -= 1
                newWeight = int(input('Enter the new weight for ' + myCourse.categories[catChoice] + ': '))
                myCourse.edit(myCourse.categories[catChoice], newWeight)
        # Allows the user to update the weights dictionary by reading the text file
            elif subMenuChoice == 3:
                myCourse.read_weights()
                print('The new weights have been read')
        # Allows the user to create a text file from the weights dictionary
            elif subMenuChoice == 4:
                myCourse.write_weights()
                print(f'The weights from the dictionary have been written into "{myCourse.FILENAME}"')
        # Allows the user to view the weight of an individual category
            elif subMenuChoice == 5:
                print(myCourse)
                weightChoice = int(input('Enter the number of the category you want to see the weight of: '))
                weightChoice -= 1
                print(f'Your current {myCourse.categories[weightChoice]} weight is '
                      f'{myCourse.get_weights(myCourse.categories[weightChoice]) * 100}%')
        # Allows the user to set the weights of each category
            elif subMenuChoice == 6:
                myCourse.set_weights()
                myCourse.write_weights()
    # Course Grades menu options
        elif menuChoice == 2:
            grade_menu()
            subMenuChoice = int(input('Menu Selection: '))
        # Displays the course categories and their grades
            if subMenuChoice not in validGradeMenu:
                print('Invalid Menu Selection')
            elif subMenuChoice == 7:
                break
            elif subMenuChoice == 1:
                myGrades.display_grades()
        # Allows the user to edit new grades for a category
            elif subMenuChoice == 2:
                myGrades.display_grades()
                grade_list = []
                catChoice = int(input('Enter the number of the category you want to edit: '))
                catChoice -= 1
                numGrades = int(input('How many grades are you overwriting?: '))
                for i in range(numGrades):
                    newGrade = float(input('Enter the new grade for ' + myGrades.categories[catChoice] + ': '))
                    grade_list.append(newGrade)
                myGrades.edit_grades(myGrades.categories[catChoice], copy.deepcopy(grade_list))
                myGrades.write_grades()
                grade_list.clear()
        # Reads in new grades from a text file
            elif subMenuChoice == 3:
                myGrades.read_grades()
                print('The new grades have been read')
        # Writes the grades from the dictionary into the text file
            elif subMenuChoice == 4:
                myGrades.write_grades()
                print(f'The grades from the dictionary have been written into "{myGrades.FILENAME}"')
            elif subMenuChoice == 5:
                print(myGrades)
                gradeChoice = int(input('Enter the number of the category you want to see the grades of: '))
                gradeChoice -= 1
                print(f'Your current {myCourse.categories[gradeChoice]} weight is '
                      f'{myGrades.get_grades(myGrades.categories[gradeChoice])}')
            elif subMenuChoice == 6:
                myGrades.set_grades()
                myGrades.write_grades()
    # Calculates Final Grade
        elif menuChoice == 3:
            myGrades.calc_grade()
