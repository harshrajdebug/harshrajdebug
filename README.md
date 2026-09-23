### Harsh Raj

I work on Kubernetes internals and security, mostly in CNCF projects: controllers, admission, policy engines and autoscaling.

Currently contributing to [OpenKruise](https://github.com/openkruise/agents/pull/1001), [PipeCD](https://github.com/pipe-cd/pipecd/pull/7412) and [kgateway](https://github.com/kgateway-dev/kgateway/pull/14749).

Some of my work:

- Fixed a gRPC connection leak in KEDA's external scaler ([#8193](https://github.com/kedacore/keda/pull/8193))
- Made the Kyverno CLI evaluate namespaced validating policies, which were passing while checking nothing ([#17608](https://github.com/kyverno/kyverno/pull/17608), backported in [#17612](https://github.com/kyverno/kyverno/pull/17612))
- Built [sigstore-guard](https://github.com/harshrajdebug/sigstore-guard), an admission webhook that only lets in pods whose images are signed by an accepted signer

<sub>B.Tech CSE (Cybersecurity and Forensics), UPES · harshrajdebug@gmail.com</sub>
