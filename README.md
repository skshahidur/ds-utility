ds-utility
==============================

Utility functions for Data Science related works

### MLFlow scikit-learn

#
#### classification_report as image

```python
from ds_utility.mlflow.sklearn_utils import classification_report_mlflow

y_true = [ "a", "d", "a", "c", "c", "a", "a", "b", "d", "c", "a", "a", "a", "a", "d",]
y_pred = [ "a", "d", "a", "a", "d", "b", "c", "a", "a", "b", "b", "c", "b", "d", "c",]
classification_report_mlflow(real, pred)
```
![classification_report](https://github.com/skshahidur/ds-utility/blob/e872a71ef92f7f72b12e74de2773be6c3a95151b/tests/assets/expected/classification_report.png)
