I go looking for the bugs that hide inside Kubernetes controllers, schedulers and policy engines: a crash loop set off by one typo, a rollback that reports Synced while the old version keeps running, a policy that passes because it never ran at all. Then I trace each one to its root, prove it, and fix it upstream.

So far that's **17 fixes merged** across [Kyverno](https://github.com/kyverno/kyverno/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged), [PipeCD](https://github.com/pipe-cd/pipecd/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged), [KEDA](https://github.com/kedacore/keda/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged), [Volcano](https://github.com/volcano-sh/volcano/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged), [Kubeflow](https://github.com/kubeflow/trainer/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged), [kgateway](https://github.com/kgateway-dev/kgateway/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged) and [Prowler](https://github.com/prowler-cloud/prowler/pulls?q=is%3Apr+author%3Aharshrajdebug+is%3Amerged), with 21 more in review.

#### A few I'm glad I caught

- **One policy could take down Kyverno's webhook.** A MutatingPolicy whose JSON patch held a list of object initializers panicked the process, and every admission request it was serving failed with it ([#17620](https://github.com/kyverno/kyverno/pull/17620), backported in [#18156](https://github.com/kyverno/kyverno/pull/18156)).
- **Kyverno's CLI approved what it never checked.** Namespaced validating policies passed without being evaluated ([#17608](https://github.com/kyverno/kyverno/pull/17608), backported in [#17612](https://github.com/kyverno/kyverno/pull/17612)), and every MutatingPolicy result was counted twice ([#17838](https://github.com/kyverno/kyverno/pull/17838)).
- **kgateway turned away SPIFFE backends.** Every SAN entry was compared as a DNS name, so a backend identified by a URI, IP or email got a 503 on every connection while its policy still reported Accepted ([#14760](https://github.com/kgateway-dev/kgateway/pull/14760)).
- **KEDA leaked gRPC connections.** The external scaler kept its pooled connections open after the last scaler using them was gone ([#8193](https://github.com/kedacore/keda/pull/8193), tests in [#8213](https://github.com/kedacore/keda/pull/8213)).
- **A PipeCD rollback that said it was done.** ECS rollbacks reported Synced while the service was still running the old revision ([#7412](https://github.com/pipe-cd/pipecd/pull/7412)).
- **Cancelling a PipeCD Terraform stage locked the state.** The apply was killed mid-run and the remote state lock stayed held; now the stage interrupts Terraform so it can let go cleanly ([#7440](https://github.com/pipe-cd/pipecd/pull/7440)).
- **One typo crash-looped Volcano.** A missing or misspelled UFM endpoint brought down the controller manager, and the Job, Queue and PodGroup controllers went down with it ([#6057](https://github.com/volcano-sh/volcano/pull/6057)).
- **Kubeflow accepted jobs that could never run.** Invalid OptimizationJob names got through, and long names produced colliding service names ([#4155](https://github.com/kubeflow/trainer/pull/4155)).
- **Prowler missed a wide-open door.** A security group allowing 0.0.0.0/1 and 128.0.0.0/1 lets in the entire internet, yet it passed the internet-exposure checks ([#13191](https://github.com/prowler-cloud/prowler/pull/13191)).

<details>
<summary><b>Still in review</b> (21 open PRs)</summary>
<br>

- **PipeCD:** restarting piped mid-deployment cancelled it and ran the rollback ([#7443](https://github.com/pipe-cd/pipecd/pull/7443)); one failing cluster cancelled every other target of a multi-cluster stage ([#7495](https://github.com/pipe-cd/pipecd/pull/7495)); a stage's skip config was applied to rollback stages by position ([#7499](https://github.com/pipe-cd/pipecd/pull/7499)); renaming the app config file left every deployment pending forever ([#7501](https://github.com/pipe-cd/pipecd/pull/7501)); plus [#7527](https://github.com/pipe-cd/pipecd/pull/7527) and [#7528](https://github.com/pipe-cd/pipecd/pull/7528)
- **Volcano:** the scheduler config from the v1.15.0 release notes made gang reclaim evict the same job endlessly ([#6046](https://github.com/volcano-sh/volcano/pull/6046)); a negative minResources panicked the scheduler ([#6189](https://github.com/volcano-sh/volcano/pull/6189)); plus [#6002](https://github.com/volcano-sh/volcano/pull/6002), [#6064](https://github.com/volcano-sh/volcano/pull/6064) and [#6120](https://github.com/volcano-sh/volcano/pull/6120)
- **Kyverno:** the CLI applied namespaced policies outside their own namespace ([#17831](https://github.com/kyverno/kyverno/pull/17831)); skip VAP generation when an exception needs Kyverno CEL ([#18251](https://github.com/kyverno/kyverno/pull/18251))
- **Kubeflow Trainer:** TrainJobs that pass admission but whose Pods can never start ([#4293](https://github.com/kubeflow/trainer/pull/4293))
- **KubeEdge:** offline edge nodes throwing away service account tokens that were still valid ([#7306](https://github.com/kubeedge/kubeedge/pull/7306), [#7307](https://github.com/kubeedge/kubeedge/pull/7307))
- **Others:** [kgateway #14749](https://github.com/kgateway-dev/kgateway/pull/14749), [OpenKruise #1001](https://github.com/openkruise/agents/pull/1001), [Prowler #13206](https://github.com/prowler-cloud/prowler/pull/13206), [Trivy checks #657](https://github.com/aquasecurity/trivy-checks/pull/657), [Kubernetes CSI docs #646](https://github.com/kubernetes-csi/docs/pull/646)

</details>

#### Things I've built

- [**sigstore-guard**](https://github.com/harshrajdebug/sigstore-guard): an admission webhook that keeps a pod out of the cluster unless its image is signed by a signer you trust
- [**aws-misconfig-scanner**](https://github.com/harshrajdebug/aws-misconfig-scanner): a read-only AWS scanner with 32 checks mapped to CIS and Security Hub, tested against a live account
- [**phishnet**](https://github.com/harshrajdebug/phishnet): a cross-modal attention model that flags phishing pages in real time and explains why

<sub>[harshrajdebug.in](https://harshrajdebug.in) · harshrajdebug@gmail.com · [LinkedIn](https://www.linkedin.com/in/harsh2789)</sub>
