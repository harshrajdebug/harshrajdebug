I work on Kubernetes control planes: controllers, schedulers, admission and policy engines, and the failure modes that only show up once a cluster is actually running.

Mostly Go, some Python. Fixes start from a reproduction, usually on envtest or kind, and come with a test that fails without them.

#### Merged upstream

| Project | What was broken | PR |
|:--|:--|:--|
| Kyverno | One MutatingPolicy could panic the admission webhook | [#17620](https://github.com/kyverno/kyverno/pull/17620) |
| kgateway | SPIFFE, IP and email SANs were matched as DNS names, so every connection got a 503 | [#14760](https://github.com/kgateway-dev/kgateway/pull/14760) |
| PipeCD | Cancelling a Terraform stage left the remote state lock held | [#7440](https://github.com/pipe-cd/pipecd/pull/7440) |
| PipeCD | An ECS rollback reported Synced while the old revision kept running | [#7412](https://github.com/pipe-cd/pipecd/pull/7412) |
| Volcano | One config typo crash-looped the controller manager | [#6057](https://github.com/volcano-sh/volcano/pull/6057) |
| KEDA | The external scaler leaked pooled gRPC connections | [#8193](https://github.com/kedacore/keda/pull/8193) |
| Kubeflow | Jobs with invalid names were accepted but could never run | [#4155](https://github.com/kubeflow/trainer/pull/4155) |
| Prowler | A rule open to the whole internet, split as 0.0.0.0/1 + 128.0.0.0/1, went unflagged | [#13191](https://github.com/prowler-cloud/prowler/pull/13191) |

<sub>17 merged across 7 projects, 21 more in review · [see them all →](https://github.com/search?q=author%3Aharshrajdebug+is%3Apr+is%3Amerged&type=pullrequests)</sub>

#### Built

- [**sigstore-guard**](https://github.com/harshrajdebug/sigstore-guard) · an admission webhook that only lets in pods whose images are signed
- [**aws-misconfig-scanner**](https://github.com/harshrajdebug/aws-misconfig-scanner) · a read-only AWS scanner with 32 checks mapped to CIS
- [**phishnet**](https://github.com/harshrajdebug/phishnet) · explainable, real-time phishing detection

#### Lately

The gap between what a control plane accepts and what it can actually run, and the places where a tool's offline answer disagrees with the cluster's.

<sub>[harshrajdebug.in](https://harshrajdebug.in) · harshrajdebug@gmail.com · [LinkedIn](https://www.linkedin.com/in/harsh2789)</sub>
