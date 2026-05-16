import unittest
import pathlib

class TestBase(unittest.TestCase):
    # 開始時に必ず走る処理
    def setUp(self):
        self.data_path = pathlib.Path('/tmp/data') 
    # 終了時に必ず走る処理
    def tearDown(self):
        for file in self.data_path.iterdir():
            file.unlink() #setupで作ったファイルを削除

class TestReadData1(TestBase):
    def setUp(self):
        super().setUp()
        p1 = self.data_path / 'data1.txt'
        p1.touch()
        p2 = self.data_path / 'data2.txt'
        p2.touch()

    def test_read_data(self):
        print(len(list(self.data_path.iterdir())))
        #ファイル数が正しいことを確認
        self.assertEqual(len(list(self.data_path.iterdir())), 2)

class TestReadData2(TestBase):
    def setUp(self):
        super().setUp()
        p3 = self.data_path / 'data3.txt'
        p3.touch()

    def test_read_data(self):
        #ファイル数が正しいことを確認 前の処理で初期化されているので1つになっていることを確認
        self.assertEqual(len(list(self.data_path.iterdir())), 1)


if __name__ == '__main__':
    unittest.main()
