# College NIRF Rank Predictor using ML

This project is an end-to-end machine learning solution that predicts the NIRF rank of a college based on various parameters such as Teaching, Learning and Resources (TLR) score, Research and Professional Practice (RPC) score, Graduation Outcomes (GO) score, Outreach and Inclusivity (OI) score, Perception score, and Peer Perception score.

I used a 2020 NIRF ranking dataset from Kaggle and implemented the project using Flask to create a simple API service that anyone can use to make predictions. The model achieved a score of 93% and a root mean square error of 15.47, which demonstrates its accuracy in predicting college NIRF rankings.

## Getting Started

### Prerequisites

To run the project, you must have the following installed on your system:

* Python 3.x
* Flask
* Pandas
* Scikit-learn

You can install the required packages using the following command:
pip install -r requirements.txt

### Required parameters
The required parameters are:

* `tlr` - Teaching, Learning and Resources score (float)
* `rpc` - Research and Professional Practice score (float)
* `go` - Graduation Outcomes score (float)
* `oi` - Outreach and Inclusivity score (float)
* `perception` - Perception score (float)
* `peer_perception` - Peer Perception score (float)

