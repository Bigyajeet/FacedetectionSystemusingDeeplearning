
-----

# Face Detection System using Deep Learning

## 🌟 Overview

This repository presents a complete **Face Detection System** built with Deep Learning. The project showcases an end-to-end machine learning pipeline, from custom data acquisition using common household technology to the training and evaluation of a robust face detection model.

The system is designed to accurately identify and localize human faces within images, leveraging the power of Convolutional Neural Networks (CNNs) and practical data collection strategies.

## ✨ Features

  * **Custom Data Collection:** Innovative use of the **IP Webcam** mobile application to capture diverse facial datasets directly from a smartphone camera, enabling flexible and accessible data generation.
  * **Efficient Data Preparation:** Raw image data is pre-processed and then serialized using Python's `pickle` module, optimizing data loading for subsequent training phases. Data is stored in a dedicated `clean_data` folder.
  * **Deep Learning Model Training:** A deep learning model is trained in a **Jupyter Notebook (`.ipynb`)** environment, providing an interactive and reproducible workflow for model development, training, and evaluation.
  * **Modular Design:** The project workflow is neatly compartmentalized:
      * Data collection and initial pickling are managed via a Python script (likely developed in Spyder).
      * Model training and experimentation are handled within a Jupyter Notebook.

## 🛠️ Technologies Used

  * **Python 3.x**
  * **Deep Learning Frameworks:** TensorFlow / Keras (Commonly used for `.ipynb` training)
  * **Data Manipulation:** NumPy, `pickle`
  * **Image Processing:** OpenCV (`cv2`)
  * **Development Environments:** Spyder IDE, Jupyter Notebook
  * **Mobile Application:** IP Webcam (Android/iOS)

## 🚀 Getting Started

Follow these instructions to set up the project and get the face detection system running on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

  * **Python 3.x**
  * **Git**
  * **Anaconda/Miniconda (Recommended)** for easy environment management.
  * **IP Webcam app** installed on your smartphone (available for Android and iOS).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Bigyajeet/FacedetectionSystemusingDeeplearning.git
    cd FacedetectionSystemusingDeeplearning
    ```

2.  **Create and activate a virtual environment (highly recommended):**

    ```bash
    conda create -n face_detect python=3.9 # Use your preferred Python version
    conda activate face_detect
    ```

    Alternatively, using `venv`:

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: .\venv\Scripts\activate
    ```



    *(**Note:** Ensure you have a `requirements.txt` file in your root directory listing all dependencies. If not, you can generate one by running `pip freeze > requirements.txt` after installing your project's dependencies manually.)*

### Usage Workflow

The project follows a sequential workflow:

#### 1\. Data Collection (using IP Webcam & Python Script)

  * **Smartphone Setup:**
      * Install and open the IP Webcam app on your phone.
      * Start the server within the app. Note down the displayed **IPv4 Address and Port** (e.g., `http://192.168.1.5:8080`).
  * **Run Collection Script:**
      * Navigate to your `data_collection_scripts/` directory.
      * Open `data_collector.py` (or similar script name) in Spyder or your preferred text editor.
      * **Crucially, modify the script** to use the IP address and port from your IP Webcam app.
      * Run the script to capture and save raw images of faces into your designated data folder.

#### 2\. Data Preprocessing & Pickling (Python Script)

  * After collecting raw images, a dedicated script (e.g., `clean_and_pickle_data.py` - this might be part of or separate from the collection script) will:
      * Load the raw images.
      * Perform any necessary preprocessing steps (e.g., resizing, converting to grayscale, normalization).
      * Serialize the cleaned and processed image data into `.pkl` (pickle) files.
      * These `.pkl` files will be saved into the `clean_data/` directory, ready for model training.

#### 3\. Model Training (Jupyter Notebook)

  * Open Jupyter Notebook from your project's root directory:
    ```bash
    jupyter notebook
    ```
  * Navigate to the `notebooks/` directory and open `train_model.ipynb` (or your specific training notebook).
  * Execute the cells sequentially within the notebook:
      * The notebook will load the pre-processed data from `clean_data/`.
      * It defines the Deep Learning model architecture (e.g., a CNN).
      * It trains the model on your prepared dataset.
      * Evaluates the trained model's performance.
      * Finally, it saves the trained model's weights and architecture (e.g., as `trained_face_detector.h5` or `model.pth`) into the `models/` directory for future inference.

## 📂 Project Structure

```
.
├── clean_data/                       # Contains pickled (.pkl) files of cleaned, pre-processed image data.
├── data_collection_scripts/          # Python scripts dedicated to raw image capture via IP Webcam.
│   └── data_collector.py             # Example: Script to connect to IP Webcam and save images.
├── notebooks/                        # Jupyter Notebooks for all deep learning model development.
│   └── train_model.ipynb             # Main notebook for defining, training, and evaluating the model.
├── models/                           # Directory to store the saved trained model weights/architecture.
│   └── trained_face_detector.h5      # Example: A saved Keras/TF model.
├── requirements.txt                  # Lists all Python package dependencies for the project.
├── README.md                         # This comprehensive project description file.
└── .gitignore                        # Specifies files/directories to be ignored by Git.
```

## ⚠️ Important Note for Git Users

During initial setup or when trying to merge divergent histories, you might encounter a `fatal: refusing to merge unrelated histories` error. This happens when your local repository and the remote repository on GitHub have no common commit ancestor.

**If you encounter this error during `git pull`:**

You can resolve it by explicitly allowing the merge of unrelated histories:

```bash
git pull origin main --allow-unrelated-histories
```

After this, Git will attempt to merge the two histories. You might need to resolve merge conflicts if files exist and have been modified in both histories. Once resolved, commit the merge, and you should then be able to `git push origin main` successfully.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\! Feel free to check the [issues page](https://www.google.com/search?q=https://github.com/Bigyajeet/FacedetectionSystemusingDeeplearning/issues).

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.


## 📞 Contact

Bigyajeet - (https://www.linkedin.com/in/bigyajeet-kumar-patra-307b85287/)

Project Link: [https://github.com/Bigyajeet/FacedetectionSystemusingDeeplearning.git](https://github.com/Bigyajeet/FacedetectionSystemusingDeeplearning.git)

-----


