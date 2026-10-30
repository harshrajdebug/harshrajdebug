I work on Kubernetes control planes: controllers, schedulers, admission and policy engines, and the failure modes that only show up once a cluster is actually running.

Mostly Go, some Python. Fixes start from a reproduction, usually on envtest or kind, and come with a test that fails without them.

#### Upstream

**[Kyverno](https://github.com/kyverno/kyverno/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged)** · Go / CEL

6 merged. A MutatingPolicy whose JSON patch holds a list of object initializers no longer panics the admission webhook and the reports controller ([#17620](https://github.com/kyverno/kyverno/pull/17620), backported to release-1.19 in [#18156](https://github.com/kyverno/kyverno/pull/18156)). In the CLI, namespaced validating policies are evaluated instead of passing unchecked ([#17608](https://github.com/kyverno/kyverno/pull/17608), [#17612](https://github.com/kyverno/kyverno/pull/17612)), and each MutatingPolicy result is counted once ([#17838](https://github.com/kyverno/kyverno/pull/17838)). Also fixed the image-verification conformance asserts that had main failing ([#17916](https://github.com/kyverno/kyverno/pull/17916)).

**[PipeCD](https://github.com/pipe-cd/pipecd/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged)** · Go / Terraform / ECS / Helm

5 merged. ECS rollback task sets are tagged with the running commit, so a rollback no longer reports Synced on the old revision ([#7412](https://github.com/pipe-cd/pipecd/pull/7412)). A cancelled Terraform stage interrupts the apply instead of killing it, which releases the remote state lock ([#7440](https://github.com/pipe-cd/pipecd/pull/7440)). The Terraform livestate respects `driftDetectionEnabled` ([#7463](https://github.com/pipe-cd/pipecd/pull/7463)), Helm charts from insecure repositories template again ([#7477](https://github.com/pipe-cd/pipecd/pull/7477)), and a multi-target's `kubectlVersion` is used by sync, canary clean and livestate ([#7525](https://github.com/pipe-cd/pipecd/pull/7525)).

Open: a piped restart mid-stage no longer cancels the deployment into a rollback ([#7443](https://github.com/pipe-cd/pipecd/pull/7443)), one failing cluster no longer cancels the other targets of a multi-cluster stage ([#7495](https://github.com/pipe-cd/pipecd/pull/7495)), skip config stays on the stage it belongs to ([#7499](https://github.com/pipe-cd/pipecd/pull/7499)), and deployments survive a renamed app config ([#7501](https://github.com/pipe-cd/pipecd/pull/7501)), plus [#7527](https://github.com/pipe-cd/pipecd/pull/7527) and [#7528](https://github.com/pipe-cd/pipecd/pull/7528).

**[KEDA](https://github.com/kedacore/keda/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged)** · Go / gRPC

2 merged. The external scaler's pool closes a gRPC connection once the last scaler using it closes ([#8193](https://github.com/kedacore/keda/pull/8193)); follow-up tests pin the pool lifecycle and the TLS error path ([#8213](https://github.com/kedacore/keda/pull/8213)).

**[Volcano](https://github.com/volcano-sh/volcano/pulls?q=is%3Apr+author%3Aharshrajdebug)** · Go

1 merged. A missing or non-string UFM endpoint in the HyperNode discovery config no longer panics the controller manager, which had taken the Job, Queue and PodGroup controllers down with it ([#6057](https://github.com/volcano-sh/volcano/pull/6057)).

Open: gang reclaim evicting the same job forever under the scheduler config from the v1.15.0 release notes ([#6046](https://github.com/volcano-sh/volcano/pull/6046)), a negative `minResources` panicking the scheduler ([#6189](https://github.com/volcano-sh/volcano/pull/6189)), HyperNode member matching ([#6002](https://github.com/volcano-sh/volcano/pull/6002)), namespace queue metrics ([#6064](https://github.com/volcano-sh/volcano/pull/6064)) and colocation config ties ([#6120](https://github.com/volcano-sh/volcano/pull/6120)).

**[Kubeflow Trainer](https://github.com/kubeflow/trainer/pulls?q=is%3Apr+author%3Aharshrajdebug)** · Go

1 merged. OptimizationJob names are validated at admission, and algorithm service names stay unique after truncation ([#4155](https://github.com/kubeflow/trainer/pull/4155)). Open: rejecting TrainJob env names and resources that a Pod can never accept ([#4293](https://github.com/kubeflow/trainer/pull/4293)).

**[kgateway](https://github.com/kgateway-dev/kgateway/pulls?q=is%3Apr+author%3Aharshrajdebug)** · Go / Envoy

1 merged. `verifySubjectAltNames` entries are matched against the right SAN type, so URI (SPIFFE), IP and email identities verify instead of failing every connection with a 503 ([#14760](https://github.com/kgateway-dev/kgateway/pull/14760)). Open: validating the `ca.crt` of a TLS secret ([#14749](https://github.com/kgateway-dev/kgateway/pull/14749)).

**[Prowler](https://github.com/prowler-cloud/prowler/pulls?q=is%3Apr+author%3Aharshrajdebug)** · Python / AWS

1 merged. Security group checks treat CIDRs that together cover the whole address space, like 0.0.0.0/1 plus 128.0.0.0/1, as open to the internet ([#13191](https://github.com/prowler-cloud/prowler/pull/13191)). Open: managed prefix lists in the same checks ([#13206](https://github.com/prowler-cloud/prowler/pull/13206)).

Also open: KubeEdge edge nodes keeping valid cached service account tokens while offline ([#7306](https://github.com/kubeedge/kubeedge/pull/7306), [#7307](https://github.com/kubeedge/kubeedge/pull/7307)), [OpenKruise #1001](https://github.com/openkruise/agents/pull/1001), [Trivy checks #657](https://github.com/aquasecurity/trivy-checks/pull/657), [Kubernetes CSI docs #646](https://github.com/kubernetes-csi/docs/pull/646).

#### Built

**[sigstore-guard](https://github.com/harshrajdebug/sigstore-guard)** · Go / Sigstore

A validating admission webhook that admits a pod only when its images carry a Sigstore signature from an accepted signer.

**[aws-misconfig-scanner](https://github.com/harshrajdebug/aws-misconfig-scanner)** · Python / AWS

A read-only scanner with 32 checks mapped to CIS AWS Foundations and Security Hub, multi-account, validated on a live account and against Prowler.

**[phishnet](https://github.com/harshrajdebug/phishnet)** · Python / PyTorch / FastAPI

A cross-modal attention model for explainable, real-time phishing detection.

#### Lately

The gap between what a control plane accepts and what it can actually run, and the places where a tool's offline answer disagrees with the cluster's.

<sub>[harshrajdebug.in](https://harshrajdebug.in) · harshrajdebug@gmail.com · [LinkedIn](https://www.linkedin.com/in/harsh2789)</sub>
