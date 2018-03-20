import unittest
from JointAssessmentFinalv5 import main, joint_assessment, individual


class test_individual_assessment(unittest.TestCase):
    def test_case01(self):
        self.assertEqual((individual(320000,240000)), 5170)

    def test_case02(self):
        self.assertEqual((individual(12000, 3000000)), 451510)

    def test_case03(self):
        self.assertEqual((individual(388392, 40000)), 7536.64)

    def test_case04(self):
        self.assertEqual((individual(500000, 450000)), 44520)

    def test_case05(self):
        self.assertEqual((individual(800000, 180000)), 77705)

    def test_case06(self):
        self.assertEqual((individual(150000, 180000)), 247.5)

    def test_case07(self):
        self.assertEqual((individual(12, 180000)), 195)

    def test_case08(self):
        self.assertEqual((individual(160000, 480000)), 2321.00)   #AssertionError: 26510.0 != 23210.0

    def test_case09(self):
        self.assertEqual((individual(102040505, 180)), 17288395.85)

    def test_case10(self):
        self.assertEqual((individual(64000, 80000)), 0)


class TestJoint_assessment(unittest.TestCase):
    def test_case01(self):
        self.assertEqual(joint_assessment(320000,240000),12230)

    def test_case02(self):
        self.assertEqual(joint_assessment(12000, 3000000), 431008)

    def test_case03(self):
        self.assertEqual(joint_assessment(388392, 40000), 2889.16)

    def test_case04(self):
        self.assertEqual(joint_assessment(500000, 450000), 78020)

    def test_case05(self):
        self.assertEqual(joint_assessment(800000, 180000), 84140)

    def test_case06(self):
        self.assertEqual(joint_assessment(150000, 180000), 303.75)

    def test_case07(self):
        self.assertEqual(joint_assessment(12, 180000), 0)

    def test_case08(self):
        self.assertEqual(joint_assessment(160000, 480000), 26510.00)

    def test_case09(self):
        self.assertEqual(joint_assessment(102040505, 180), 100)  #AssertionError: 17265984.92 != 100

    def test_case10(self):
        self.assertEqual(joint_assessment(64000, 80000), 0)

class test_recommend(unittest.TestCase):
    def test_case01(self):
        print("case 1")
        self.assertEqual(main(320000, 240000), "Choose Individual for lower tax payable.")

    def test_case02(self):
        print("case 2")
        self.assertEqual(main(12000, 3000000), "Choose Joint Assessment for lower tax payable.")

    def test_case03(self):
        print("case 3")
        self.assertEqual(main(388392, 40000), "Choose Joint Assessment for lower tax payable.")

    def test_case04(self):
        print("case 4")
        self.assertEqual(main(500000, 450000), "Choose Individual for lower tax payable.")

    def test_case05(self):
        print("case 5")
        self.assertEqual(main(800000, 180000), "Choose Individual for lower tax payable.")

    def test_case06(self):
        print("case 6")
        self.assertEqual(main(150000, 180000), "Choose Individual for lower tax payable.")

    def test_case07(self):
        print("case 7")
        self.assertEqual(main(12, 180000), "Choose Joint Assessment for lower tax payable.")

    def test_case08(self):
        print("case 8")
        self.assertEqual(main(160000, 480000), "Choose Individual for lower tax payable.")

    def test_case09(self):
        print("case 9")
        self.assertEqual(main(102040505, 180), "Choose Joint Assessment for lower tax payable.")

    def test_case10(self):
        print("case 10")
        self.assertEqual(main(64000, 80000), "Choose Joint Assessment for lower tax payable.")
        #AssertionError: 'Either Joint Assessment or Individual Assessment.' != 'Choose Joint Assessment for lower tax payable.'
        #- Either Joint Assessment or Individual Assessment.
        #+ Choose Joint Assessment for lower tax payable.

if __name__ == '__main__':
    unittest.main