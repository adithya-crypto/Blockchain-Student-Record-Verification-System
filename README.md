# Blockchain Student Record Verification System

A web application that leverages Ethereum blockchain technology to securely store and verify student academic records.

## Description

This project implements a student record verification system using blockchain technology. It allows educational institutions to add student records to the Ethereum blockchain and provides a verification mechanism to validate student information.

Key features:
- Secure storage of student records on the Ethereum blockchain
- API endpoints for adding new student records
- Verification mechanism to authenticate student information
- Web interface for interacting with the blockchain contract

## Technologies Used

- **Backend**: Flask (Python)
- **Blockchain**: Ethereum
- **Web3 Interface**: Web3.py
- **Frontend**: HTML/CSS/JavaScript (implied)

## Prerequisites

- Python 3.7+
- Flask
- Web3.py
- An Ethereum wallet with ETH for transaction fees
- Infura API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/blockchain-student-records.git
   cd blockchain-student-records
   ```

2. Install dependencies:
   ```
   pip install flask web3
   ```

3. Configure the Infura API key and contract address in `backend.py` if needed.

4. Ensure you have the contract ABI file (`StudentRecordABI.json`) in the project root.

## Usage

1. Start the Flask server:
   ```
   python backend.py
   ```

2. Access the web interface at `http://localhost:5000`

3. To add a student record, send a POST request to `/add_record` with the following JSON structure:
   ```json
   {
     "student_id": "12345",
     "name": "John Doe",
     "grade": "A"
   }
   ```

4. To verify a student record, send a POST request to `/verify` with the same JSON structure.

## Smart Contract

The application interacts with a smart contract deployed at `0xf8e81D47203A594245E36C48e151709F0C19fBe8`. The contract provides functions for adding and verifying student records.

## Security Considerations

- This application requires an Ethereum wallet with sufficient ETH to cover transaction fees
- Proper key management and security practices should be implemented in a production environment
- The provided Infura API key should be kept confidential

## Future Enhancements

- Add authentication and authorization mechanisms
- Implement a more comprehensive student record structure
- Add batch processing for multiple student records
- Create a more interactive UI for better user experience

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
