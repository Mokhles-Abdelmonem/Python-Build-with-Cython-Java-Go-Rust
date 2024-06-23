use pyo3::prelude::*;

#[pyfunction]
fn add(a: i64, b: i64) -> PyResult<i64> {
    let mut sum = 0;
    for i in a..=b {
        sum += i;
    }
    Ok(sum)
}

#[pymodule]
fn rust_example(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    Ok(())
}
