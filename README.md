# PrintMaster

PrintMaster is a Python-based utility designed to enhance printer management on Windows. It provides features such as batch printing and print job prioritization, allowing users to efficiently manage multiple print tasks.

## Features

- **Batch Printing**: Queue multiple print jobs and process them in batches.
- **Print Job Prioritization**: Assign priority levels to print jobs to determine their order of execution.

## Requirements

- Windows operating system
- Python 3.x
- `pywin32` library (for Windows API access)

## Installation

Before running PrintMaster, ensure you have the required Python library:

```bash
pip install pywin32
```

## Usage

1. **Add Print Jobs**: Use the `add_job` method to add files to the print queue. Specify the file path and an optional priority (default is 1).

2. **Start Batch Printing**: Call the `start_batch_printing` method to begin processing the print queue.

### Example

```python
from print_master import PrintMaster

pm = PrintMaster()
pm.add_job("document1.pdf", priority=2)
pm.add_job("document2.pdf", priority=1)
pm.add_job("document3.pdf", priority=3)
pm.start_batch_printing()
```

In this example, `document3.pdf` will be printed first due to its highest priority, followed by `document1.pdf`, and finally `document2.pdf`.

## Note

- Ensure the files specified in print jobs are accessible and compatible with the default printer.
- The program simulates the printing delay; adjust the `time.sleep(5)` in the code to match your needs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.