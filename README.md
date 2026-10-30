I work on Kubernetes control planes: controllers, schedulers, admission and policy engines, and the failure modes that only show up once a cluster is actually running.

**17 fixes merged upstream** in Kyverno, PipeCD, KEDA, Volcano, Kubeflow, kgateway and Prowler.

#### Recent

- **Kyverno** · one MutatingPolicy could panic the admission webhook ([#17620](https://github.com/kyverno/kyverno/pull/17620))
- **kgateway** · SPIFFE, IP and email SANs were checked as DNS names, so every connection got a 503 ([#14760](https://github.com/kgateway-dev/kgateway/pull/14760))
- **PipeCD** · cancelling a Terraform stage left the remote state lock held ([#7440](https://github.com/pipe-cd/pipecd/pull/7440))
- **Volcano** · one config typo crash-looped the controller manager ([#6057](https://github.com/volcano-sh/volcano/pull/6057))
- **KEDA** · the external scaler leaked pooled gRPC connections ([#8193](https://github.com/kedacore/keda/pull/8193))

<sub>[All merged PRs →](https://github.com/search?q=author%3Aharshrajdebug+is%3Apr+is%3Amerged&type=pullrequests)</sub>

#### Built

- [**sigstore-guard**](https://github.com/harshrajdebug/sigstore-guard) · admission webhook that only admits pods with signed images
- [**aws-misconfig-scanner**](https://github.com/harshrajdebug/aws-misconfig-scanner) · read-only AWS scanner, 32 checks mapped to CIS
- [**phishnet**](https://github.com/harshrajdebug/phishnet) · explainable, real-time phishing detection

#### Lately

The gap between what a control plane accepts and what it can actually run, and the places where a tool's offline answer disagrees with the cluster's.

<sub>[harshrajdebug.in](https://harshrajdebug.in) · harshrajdebug@gmail.com · [LinkedIn](https://www.linkedin.com/in/harsh2789)</sub>
