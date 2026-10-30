I work on Kubernetes control planes: controllers, schedulers, admission and policy engines, and the failure modes that only show up once a cluster is actually running.

Mostly Go, some Python. Fixes start from a reproduction, usually on envtest or kind, and come with a test that fails without them.

#### Lately

The gap between what a control plane accepts and what it can actually run, and the places where a tool's offline answer disagrees with the cluster's.
