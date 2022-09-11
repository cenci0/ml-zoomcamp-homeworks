### Question 6

1. Find the median value of "Engine Cylinders" column in the dataset.
2. Next, calculate the most frequent value of the same "Engine Cylinders".
3. Use the `fillna` method to fill the missing values in "Engine Cylinders" with the most frequent value from the previous step.
4. Now, calculate the median value of "Engine Cylinders" once again.

Has it changed?

> Hint: refer to existing `mode` and `median` functions to complete the task.

- Yes
- No

---

### Answer

1. The median value in the original dataset is `6.0`.
2. The most frequent value is `4.0`.
3. _(not a question)_
4. The median value in the newly obtained dataset is still `6.0`.

The median value has not changed.
There were ~30 missing values, and given the distribution for engine cylinders on almost 12k values was likely to have
no impact on the median value. All quantiles remained unchanged.
