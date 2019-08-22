import unittest

from abi_inline_device_reader import AbiInlineDeviceReader


class MsvcAbiInlineDeviceReaderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.device_reader = AbiInlineDeviceReader(AbiInlineDeviceReader.Library.msvc)

    def test_devicereader_returns_correct_values(self):
        result_ptr = self.device_reader.get_cell(b"Device1", 0, 0)
        self.assertEqual(self.device_reader.to_string(result_ptr), b"Device1[0][0]")
        self.device_reader.free_resource(result_ptr)
        result_ptr = self.device_reader.get_cell(b"Device2", 1, 2)
        self.assertEqual(self.device_reader.to_string(result_ptr), b"Device2[1][2]")
        self.device_reader.free_resource(result_ptr)

    def test_allocated_resource_can_be_released(self):
        result_ptr = self.device_reader.get_cell(b"Device1", 0, 0)
        self.assertEqual(self.device_reader.num_allocated_resources(), 1)
        self.device_reader.free_resource(result_ptr)
        self.assertEqual(self.device_reader.num_allocated_resources(), 0)

    def test_all_allocated_resources_can_be_released(self):
        self.device_reader.get_cell(b"Device1", 0, 0)
        self.device_reader.get_cell(b"Device2", 1, 2)
        self.assertEqual(self.device_reader.num_allocated_resources(), 2)
        self.device_reader.free_resources()
        self.assertEqual(self.device_reader.num_allocated_resources(), 0)


if __name__ == "__main__":
    unittest.main()