'''
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## TODO write a test that adds and removes a student, and asserts the student is removed. Use assertNotIn
    def testAddsRemovesStudent(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)


    ## TODO write a test that adds some example students, then removes a student not in the list, and asserts a StudentError is raised
    def test_Add_Some_Remove_Student_Not_In_List(self):
        test_class = ClassList(2)
        test_class.add_student('Clif')
        test_class.add_student('Dinozo')
        test_class.add_student('Fran')
        with self.assertRaises(StudentError):
            test_class.remove_student('Fred')

    ## TODO write a test that removes a student from an empty list, and asserts a StudentError is raised
    def test_remove_student_from_empty_list_assert_StudentError(self):
        test_class = ClassList(2)
        with self.assertRaises(StudentError):
            test_class.remove_student('Frank')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart') ##Their show was so funny
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. use assertFalse to verify is_enrolled returns False.
    def test_is_enrolled_for_a_student_not_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Tony Dinozo')
        test_class.add_student('Tim McGee')
        test_class.add_student('Leroy Gibs')
        self.assertFalse(test_class.is_enrolled('Director Vance'))



    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    ## TODO write a test for index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. use assertIsNone.
    def test_index_of_student_when_class_list_is_empty(self):
        test_class = ClassList(2)
        self.assertIsNone(test_class.index_of_student('Farris Buler'))
 
    ## TODO write another test for index_of_student. In the case when the list is not empty but 
    # assert that searching for a student name that is not in the list, returns None.
    def test_index_of_student_not_empty_not_in(self):
        test_class = ClassList(2)
        test_class.add_student('Lisa Simpson')
        test_class.add_student('Bart Simpson')
        self.assertIsNone(test_class.index_of_student('Maggie Simpson'))
   
    ## TODO write a test for your new is_class_full method when the class is full. use assertTrue.
    def test_is_class_full_when_class_is_full(self):
        test_class = ClassList(2)
        test_class.add_student('Freddy Kruger')
        test_class.add_student('Jason Vorhese')
        self.assertTrue(test_class.is_class_full(2))
    
    ## TODO write a test for your new is_class_full method for when is empty, and when it is not full. Use assertFalse.
    def test_is_class_full_when_empty_and_when_its_not(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_class_full(2))
        test_class.add_student('Jerry Garcia')
        self.assertFalse(test_class.is_class_full(2))
