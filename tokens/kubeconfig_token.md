# `kubeconfig` Token
The Kubernetes configuration file is typically located under `~/.kube/config`, making it a potential target for attackers. If accessed and used by an unauthorized party, it will trigger an alert.

## Applicable Environments
Applies universally across all environments where a kubernetes config can be used, but utilities like `kubectl`.

## How The Token Gets Triggered?
The token attempted to connect using the Kubernetes configuration. On the backend, an alert mechanism is in place that triggers an alert whenever an access attempt is detected.

## How to Identify the Token Without Triggering It?
Keep the [`indicators.md`](../indicators.md) file handy, as it contains the indicators of how the file is a canary token. <!-- Do not delete this line -->

To identify whether an `kubeconfig` is a canary token, follow these steps:
1. Observe the JSON structure of the `kubeconfig` and observe the `clusters.cluster.server` value.
```yaml
apiVersion: v1
kind: Config
clusters:
- cluster:
    certificate-authority-data: LS0tL...S0tLQo=
    server: https://52.18.63.80:6443
  name: k8s-prod-cluster
users:
- name: k8s_infra_superuser
  user:
    client-certificate-data: LS0tL...S0tLQo=
    client-key-data: LS0tL...S0tLQo=
contexts:
- context:
    cluster: k8s-prod-cluster
    user: k8s_infra_superuser
  name: k8s_infra_superuser-k8s-prod-cluster
current-context: k8s_infra_superuser-k8s-prod-cluster
```
2. The IP address - `52.18.63.80`, it resolves to an address associated with `canarytokens.org`.

## Contributors
[<img src="https://github.com/0xcardinal.png" style="width:60px; height:60px;"/>](https://github.com/0xcardinal)