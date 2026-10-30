<h1 align="center">Harsh Raj</h1>

<p align="center">I find and fix bugs in Kubernetes controllers, schedulers, admission webhooks and policy engines, mostly in CNCF projects.</p>

<p align="center">
  <a href="https://harshrajdebug.in"><img alt="Website" src="https://img.shields.io/badge/harshrajdebug.in-1f6feb?style=flat-square&logo=googlechrome&logoColor=white"></a>
  <a href="mailto:harshrajdebug@gmail.com"><img alt="Email" src="https://img.shields.io/badge/harshrajdebug@gmail.com-c5221f?style=flat-square&logo=gmail&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/harsh2789"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0a66c2?style=flat-square&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAyNCAyNCcgZmlsbD0nd2hpdGUnPjxyZWN0IHg9JzMnIHk9JzknIHdpZHRoPSc0JyBoZWlnaHQ9JzEyJy8%2BPGNpcmNsZSBjeD0nNScgY3k9JzUnIHI9JzIuMicvPjxwYXRoIGQ9J00xMCA5aDMuOHYxLjdjLjYtMS4xIDItMiA0LTIgNCAwIDQuNyAyLjYgNC43IDZWMjFoLTR2LTUuNWMwLTEuNCAwLTMuMS0xLjktMy4xcy0yLjIgMS41LTIuMiAzVjIxaC00eicvPjwvc3ZnPg%3D%3D"></a>
</p>

<p align="center"><b>17 merged PRs</b> across <b>7 projects</b> · <b>21 more in review</b></p>

<p align="center">
  <img alt="Go" src="https://img.shields.io/badge/Go-00add8?style=flat-square&logo=go&logoColor=white">
  <img alt="Kubernetes" src="https://img.shields.io/badge/Kubernetes-326ce5?style=flat-square&logo=kubernetes&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776ab?style=flat-square&logo=python&logoColor=white">
  <img alt="AWS" src="https://img.shields.io/badge/AWS-232f3e?style=flat-square">
  <img alt="Envoy" src="https://img.shields.io/badge/Envoy-ac6199?style=flat-square&logo=envoyproxy&logoColor=white">
  <img alt="Terraform" src="https://img.shields.io/badge/Terraform-7b42bc?style=flat-square&logo=terraform&logoColor=white">
  <img alt="Helm" src="https://img.shields.io/badge/Helm-0f1689?style=flat-square&logo=helm&logoColor=white">
</p>

---

### Merged upstream

| Project | Merged | What the fixes cover |
|:--|:-:|:--|
| [Kyverno](https://github.com/kyverno/kyverno/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged) | 6 | Webhook crash on MutatingPolicy patches, CLI policy evaluation, conformance tests, two release backports |
| [PipeCD](https://github.com/pipe-cd/pipecd/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged) | 5 | ECS rollbacks, Terraform cancel and drift detection, Helm chart repos, multi-cluster kubectl versions |
| [KEDA](https://github.com/kedacore/keda/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged) | 2 | gRPC connection leak in the external scaler, with tests |
| [Volcano](https://github.com/volcano-sh/volcano/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged) | 1 | Controller manager crash loop on a bad HyperNode discovery config |
| [Kubeflow Trainer](https://github.com/kubeflow/trainer/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged) | 1 | OptimizationJob name validation and service name collisions |
| [kgateway](https://github.com/kgateway-dev/kgateway/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged) | 1 | Backend TLS SAN verification |
| [Prowler](https://github.com/prowler-cloud/prowler/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged) | 1 | Security groups that are open to the internet without listing 0.0.0.0/0 |

### Selected fixes

- **Kyverno webhook crash.** One MutatingPolicy whose JSON patch held a list of object initializers panicked Kyverno, taking down the mutating webhook and failing every affected admission request ([#17620](https://github.com/kyverno/kyverno/pull/17620), backported in [#18156](https://github.com/kyverno/kyverno/pull/18156)).
- **Kyverno CLI checking nothing.** The CLI passed namespaced validating policies without evaluating them ([#17608](https://github.com/kyverno/kyverno/pull/17608), backported in [#17612](https://github.com/kyverno/kyverno/pull/17612)), and counted each MutatingPolicy result twice ([#17838](https://github.com/kyverno/kyverno/pull/17838)).
- **kgateway TLS to SPIFFE backends.** SAN entries were matched as DNS names only, so backends identified by a URI, IP or email got a 503 on every connection while the policy reported Accepted ([#14760](https://github.com/kgateway-dev/kgateway/pull/14760)).
- **KEDA connection leak.** The external scaler kept pooled gRPC connections open after the last scaler using them closed ([#8193](https://github.com/kedacore/keda/pull/8193), tests in [#8213](https://github.com/kedacore/keda/pull/8213)).
- **PipeCD ECS rollbacks.** A rollback reported Synced while the service still ran the old revision ([#7412](https://github.com/pipe-cd/pipecd/pull/7412)).
- **PipeCD Terraform state locks.** Cancelling a stage killed the apply and left the remote state lock held; it now interrupts the apply so the lock is released ([#7440](https://github.com/pipe-cd/pipecd/pull/7440)).
- **Volcano controller crash loop.** A missing or misspelled UFM endpoint crash-looped the controller manager, taking the Job, Queue and PodGroup controllers down with it ([#6057](https://github.com/volcano-sh/volcano/pull/6057)).
- **Kubeflow OptimizationJobs that never ran.** Invalid names were accepted, and long names produced colliding algorithm service names ([#4155](https://github.com/kubeflow/trainer/pull/4155)).
- **Prowler missed open security groups.** A rule allowing 0.0.0.0/1 plus 128.0.0.0/1 accepts every address but passed the internet-exposure checks ([#13191](https://github.com/prowler-cloud/prowler/pull/13191)).

<details>
<summary><b>In review</b> (21 open PRs)</summary>
<br>

- **PipeCD:** restarting piped mid-deployment cancelled it and ran the rollback ([#7443](https://github.com/pipe-cd/pipecd/pull/7443)); one failing cluster cancelled every other target of a multi-cluster stage ([#7495](https://github.com/pipe-cd/pipecd/pull/7495)); a stage's skip config was applied to rollback stages by position ([#7499](https://github.com/pipe-cd/pipecd/pull/7499)); renaming the app config file left every deployment pending forever ([#7501](https://github.com/pipe-cd/pipecd/pull/7501)); plus [#7527](https://github.com/pipe-cd/pipecd/pull/7527) and [#7528](https://github.com/pipe-cd/pipecd/pull/7528)
- **Volcano:** the scheduler config from the v1.15.0 release notes made gang reclaim evict the same job endlessly ([#6046](https://github.com/volcano-sh/volcano/pull/6046)); a negative minResources panicked the scheduler ([#6189](https://github.com/volcano-sh/volcano/pull/6189)); plus [#6002](https://github.com/volcano-sh/volcano/pull/6002), [#6064](https://github.com/volcano-sh/volcano/pull/6064) and [#6120](https://github.com/volcano-sh/volcano/pull/6120)
- **Kyverno:** namespaced policies applied outside their namespace in the CLI ([#17831](https://github.com/kyverno/kyverno/pull/17831)), and skipping VAP generation when an exception needs Kyverno CEL ([#18251](https://github.com/kyverno/kyverno/pull/18251))
- **Kubeflow Trainer:** TrainJobs that pass admission but whose Pods can never start ([#4293](https://github.com/kubeflow/trainer/pull/4293))
- **KubeEdge:** edge nodes discarding still-valid cached service account tokens while offline ([#7306](https://github.com/kubeedge/kubeedge/pull/7306), [#7307](https://github.com/kubeedge/kubeedge/pull/7307))
- **Others:** [kgateway #14749](https://github.com/kgateway-dev/kgateway/pull/14749), [OpenKruise #1001](https://github.com/openkruise/agents/pull/1001), [Prowler #13206](https://github.com/prowler-cloud/prowler/pull/13206), [Trivy checks #657](https://github.com/aquasecurity/trivy-checks/pull/657), [Kubernetes CSI docs #646](https://github.com/kubernetes-csi/docs/pull/646)

</details>

### Projects

| Project | What it does |
|:--|:--|
| [**sigstore-guard**](https://github.com/harshrajdebug/sigstore-guard) | Kubernetes admission webhook that only admits pods whose images are signed by an accepted Sigstore signer |
| [**aws-misconfig-scanner**](https://github.com/harshrajdebug/aws-misconfig-scanner) | Read-only AWS scanner with 32 checks mapped to CIS AWS Foundations and Security Hub, validated on a live account |
| [**phishnet**](https://github.com/harshrajdebug/phishnet) | Cross-modal attention model for explainable, real-time phishing detection |
