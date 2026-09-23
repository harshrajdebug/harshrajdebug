### Harsh Raj

I work on Kubernetes internals and security: controllers, admission and policy engines, autoscaling, and workload identity.

B.Tech Computer Science (Cybersecurity and Forensics) at UPES, Dehradun, graduating 2027.

**Merged**

- [kedacore/keda#8193](https://github.com/kedacore/keda/pull/8193): the external scaler's gRPC connection pool never released an entry, so every scaler address and TLS combination kept a connection and a goroutine for the life of the process.
- [kyverno/kyverno#17608](https://github.com/kyverno/kyverno/pull/17608), backported in [#17612](https://github.com/kyverno/kyverno/pull/17612): the CLI resolved no resource kinds for namespaced validating policies, so they passed while checking nothing.

**Open**

- [pipe-cd/pipecd#7412](https://github.com/pipe-cd/pipecd/pull/7412): ECS rollbacks were reported as synced while running the previous revision.
- [openkruise/agents#1001](https://github.com/openkruise/agents/pull/1001): claim labels could overwrite labels the sandbox controller owns.
- [kyverno/kyverno#17620](https://github.com/kyverno/kyverno/pull/17620): an unrecovered panic in MutatingPolicy JSON patches that crashed the mutating webhook.
- [kubeedge/kubeedge#7306](https://github.com/kubeedge/kubeedge/pull/7306) and [#7307](https://github.com/kubeedge/kubeedge/pull/7307): offline edge nodes failing to start pods that mount a service account token.
- [volcano-sh/volcano#6002](https://github.com/volcano-sh/volcano/pull/6002): require exact matching for HyperNode-typed members.

**Project**

- [sigstore-guard](https://github.com/harshrajdebug/sigstore-guard): a Kubernetes validating admission webhook that rejects pods whose images carry no Sigstore signature from an accepted signer, with the trust root anchored in TUF.

Go, Kubernetes, gRPC, controller-runtime, Sigstore, Python, PyTorch.
