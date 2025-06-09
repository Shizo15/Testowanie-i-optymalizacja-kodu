from clearml.automation import UniformParameterRange, DiscreteParameterRange, HyperParameterOptimizer
from clearml import Task

task = Task.init(
    project_name='TiOp project',
    task_name='Hyperparameter Optimization v3',
    task_type=Task.TaskTypes.optimizer
)

BASE_TASK_ID = '24ebbc04e92a41449fd44ef2ddeb97ba'

optimizer = HyperParameterOptimizer(
    base_task_id=BASE_TASK_ID,
    hyper_parameters=[
        UniformParameterRange("batch_size", min_value=16, max_value=64, step_size=16),
        UniformParameterRange("dropout", min_value=0.0, max_value=0.5, step_size=0.1),
        UniformParameterRange("img_shape", min_value=64, max_value=224, step_size=32),  # 64x64, 96x96, etc.
        UniformParameterRange("epochs", min_value=5, max_value=15, step_size=5),
        DiscreteParameterRange("model_name", values=["resnet50", "resnet101", "mobilenet", "vgg16"]),
        DiscreteParameterRange("transfer_learning", values=[True, False]),
        DiscreteParameterRange("normalization", values=[True, False]),
        DiscreteParameterRange("augmentation", values=[True, False]),
        DiscreteParameterRange("extra_data", values=[True, False])

    ],
    objective_metric_title='Accuracy',
    objective_metric_series='val',
    objective_metric_sign='max',
    max_number_of_concurrent_tasks=2,
    execution_queue='default',
)

optimizer.set_report_period(0.5)
optimizer.set_time_limit(in_minutes=30)

optimizer.start()

optimizer.wait()
optimizer.stop()

top_exp = optimizer.get_top_experiments(top_k=1)[0]
best_params = top_exp.get_parameters()

print("\n=== Najlepszy eksperyment ===")
print(f"Task ID: {top_exp.id}")
print("Hiperparametry:")
for key, value in best_params.items():
    print(f"  {key}: {value}")

metrics = top_exp.get_last_scalar_metrics()
val_acc = metrics.get("Accuracy", {}).get("val", {}).get("value", "brak danych")

print(f"Najlepsza val_accuracy: {val_acc}")

