### Hi, I'm Harsh

I work on Kubernetes internals and security: controllers, admission webhooks, policy engines and autoscaling, mostly in CNCF projects. Every fix below ships with a test that covers it.

Final-year B.Tech student in Computer Science (Cybersecurity and Forensics) at UPES, Dehradun, graduating 2027.

#### Open source

| Pull request | What was wrong | Status |
|---|---|---|
| [kedacore/keda#8193](https://github.com/kedacore/keda/pull/8193) | The external scaler's gRPC connection pool never released an entry, so every scaler address and TLS combination kept a connection and a goroutine for the life of the process | Merged |
| [kyverno/kyverno#17608](https://github.com/kyverno/kyverno/pull/17608) | The CLI resolved no resource kinds for namespaced validating policies, so they passed while checking nothing | Merged, backported to 1.19 in [#17612](https://github.com/kyverno/kyverno/pull/17612) |
| [pipe-cd/pipecd#7412](https://github.com/pipe-cd/pipecd/pull/7412) | ECS rollbacks were reported as synced while running the previous revision | Open |
| [openkruise/agents#1001](https://github.com/openkruise/agents/pull/1001) | Claim labels could overwrite labels the sandbox controller owns | Open |
| [kyverno/kyverno#17620](https://github.com/kyverno/kyverno/pull/17620) | An unrecovered panic in MutatingPolicy JSON patches crashed the mutating webhook | Open |
| [kubeedge/kubeedge#7306](https://github.com/kubeedge/kubeedge/pull/7306), [#7307](https://github.com/kubeedge/kubeedge/pull/7307) | Offline edge nodes could not start pods that mount a service account token | Open |
| [volcano-sh/volcano#6002](https://github.com/volcano-sh/volcano/pull/6002) | HyperNode-typed members were not required to use exact matching | Open |

I also review other contributors' pull requests. On PipeCD, [#7410](https://github.com/pipe-cd/pipecd/pull/7410#pullrequestreview-5292490556) and [#7409](https://github.com/pipe-cd/pipecd/pull/7409#pullrequestreview-5292490808), I found that an exact body match fails against JSON health endpoints ending in a newline, and that a new validation would stop whole applications from deploying.

#### Project

**[sigstore-guard](https://github.com/harshrajdebug/sigstore-guard)** [![ci](https://github.com/harshrajdebug/sigstore-guard/actions/workflows/ci.yml/badge.svg)](https://github.com/harshrajdebug/sigstore-guard/actions/workflows/ci.yml)

A Kubernetes validating admission webhook that rejects pods whose images carry no Sigstore signature from an accepted signer.

- The trust root is anchored in TUF and refreshed every six hours, so a Sigstore key rotation reaches the cluster without a redeploy.
- The API server's failurePolicy and the policy's own failOpen are kept as separate controls, one for an unreachable webhook and one for an unreachable registry or TUF.
- CI runs unit tests with the race detector, live checks against the public Sigstore infrastructure, and end-to-end tests on a kind cluster.

#### Tools

Go, Kubernetes, gRPC, controller-runtime, Sigstore, Python, PyTorch
