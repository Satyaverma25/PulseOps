# Performance Budget Report  
DevOps Intern Take-Home Assignment – 10x Construction  
Candidate: Satya

---

## 1. Introduction

This report documents the analysis, optimization, and observability design of a Python-based sensor service provided as part of the DevOps Intern assignment.

The objective was to deploy the service in a resource-constrained environment, identify performance bottlenecks, reduce CPU and memory overhead, and design a lightweight observability stack while staying within a strict memory budget.

---

## 2. Memory Usage of Each Component (Before vs After)

### Before Optimization

The original Python sensor service performed heavy computation and large in-memory allocations inside the `/metrics` endpoint.  
Since this endpoint is frequently scraped by Prometheus, this design could lead to unbounded memory growth, CPU spikes, and scrape delays.

Exact memory numbers were not captured before optimization, as the service did not have instrumentation at that stage.  
However, observed behavior such as high CPU usage, inconsistent response times, and unstable scrapes clearly indicated inefficient resource usage.

### After Optimization

After refactoring the service and containerizing the full stack, memory usage was measured using `docker stats`.

| Component        | Memory Usage (Approx.) |
|------------------|------------------------|
| Sensor Service   | ~27 MB                 |
| Prometheus       | ~28 MB                 |
| Grafana          | ~120 MB                |
| **Total**        | **~175 MB**            |

The complete observability stack runs comfortably within the **300 MB memory limit** defined in the assignment.

---

## 3. Identified Bottlenecks in the Python Service

The following bottlenecks were identified during analysis:

- Heavy synchronous loops inside the `/metrics` endpoint  
- Large data allocations during metrics collection  
- Blocking behavior during Prometheus scrapes  
- Tight coupling between simulation logic and observability logic  

These issues resulted in CPU spikes, increased memory pressure, scrape delays, and intermittent dashboard instability.

---

## 4. Code-Level Optimizations

To address the identified issues:

- The metrics endpoint was kept lightweight and non-blocking  
- Only essential metrics were exposed  
- Expensive computation was reduced during scrapes  
- High-cardinality metrics were avoided  

These changes stabilized CPU usage, reduced memory overhead, and improved scrape reliability.

---

## 5. Metrics System Choice (Prometheus)

**Chosen Option:** Prometheus with memory-conscious configuration

### Justification

Prometheus was selected due to its pull-based model, reliability, and native integration with Grafana.  
It is well-suited for containerized and edge-style deployments.

Memory optimization considerations included:

- Reduced scrape frequency to avoid unnecessary load  
- Minimal metric cardinality  
- Short-term observability focus rather than long retention  
- Awareness of WAL compression and tuning for constrained environments  

Prometheus-compatible alternatives such as VictoriaMetrics or OpenTelemetry Collector were evaluated conceptually.  
Prometheus was preferred for its simplicity and ease of debugging for a single-node setup.

---

## 6. Visualization Layer Choice (Grafana)

**Chosen Option:** Grafana

### Justification

Grafana was selected for its flexible visualization capabilities and seamless Prometheus integration.

To remain within memory limits:

- Dashboards were kept minimal with only essential panels  
- Time ranges were limited to short windows  
- No alerting rules or additional plugins were enabled  

Observed Grafana memory usage remained around **120 MB**, which is acceptable within the overall budget.

---

## 7. Custom Metric and Reasoning

A custom metric was added to improve observability:

- **Processing Latency Histogram**  
  This metric captures how request processing time behaves over time and highlights performance degradation under load.

This provides deeper insight than counters alone and helps correlate CPU stress with latency trends.

---

## 8. One Improvement with One More Week

If given an additional week, the following improvements would be prioritized:

- Add alerting rules for high latency and CPU usage  
- Perform structured load testing  
- Introduce asynchronous or background processing  
- Further tune scrape intervals dynamically  

These enhancements would improve resilience and production readiness.

---

## 9. Conclusion

The optimized sensor service and observability stack successfully address the performance issues present in the original implementation.

By identifying bottlenecks, applying code-level optimizations, and designing a memory-efficient observability setup, the system remains stable, debuggable, and well within resource constraints.

This solution demonstrates practical DevOps thinking suitable for real-world, resource-constrained environments.
