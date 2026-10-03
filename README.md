### About me

I work on Kubernetes internals and security, mostly in CNCF projects: controllers, admission, policy engines and autoscaling.

Merged in [Kyverno](https://github.com/kyverno/kyverno/pull/17608), [KEDA](https://github.com/kedacore/keda/pull/8193) and [PipeCD](https://github.com/pipe-cd/pipecd/pull/7412), with fixes in review at [Volcano](https://github.com/volcano-sh/volcano/pull/6046), [Kubeflow](https://github.com/kubeflow/trainer/pull/4155), [kgateway](https://github.com/kgateway-dev/kgateway/pull/14749), [OpenKruise](https://github.com/openkruise/agents/pull/1001) and [KubeEdge](https://github.com/kubeedge/kubeedge/pull/7307).

Some of my work:

- Fixed a gRPC connection leak in KEDA's external scaler ([#8193](https://github.com/kedacore/keda/pull/8193), with tests in [#8213](https://github.com/kedacore/keda/pull/8213))
- Made the Kyverno CLI evaluate namespaced validating policies, which were passing while checking nothing ([#17608](https://github.com/kyverno/kyverno/pull/17608), backported in [#17612](https://github.com/kyverno/kyverno/pull/17612))
- Fixed PipeCD ECS rollbacks that reported Synced while still running the old revision ([#7412](https://github.com/pipe-cd/pipecd/pull/7412))
- Found that the scheduler config in the Volcano v1.15.0 release notes makes gang reclaim evict the same job endlessly; fix in review ([#6046](https://github.com/volcano-sh/volcano/pull/6046))
- Found that restarting PipeCD's piped in the middle of a deployment cancelled it and ran the rollback; fix in review ([#7443](https://github.com/pipe-cd/pipecd/pull/7443))
- Built [sigstore-guard](https://github.com/harshrajdebug/sigstore-guard), an admission webhook that only lets in pods whose images are signed by an accepted signer

<sub>[harshrajdebug.in](https://harshrajdebug.in) · harshrajdebug@gmail.com</sub>
