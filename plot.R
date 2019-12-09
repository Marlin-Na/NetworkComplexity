
library(ggplot2)
library(readr)
library(tidyr)
library(dplyr)

gnp_data <- readr::read_tsv("compare_gnp_data.txt")
gnp_data <- tidyr::gather(gnp_data, key = "algorithm", value = "value", -N, -p)
gnp_data <- filter(gnp_data, p %in% c(0.05, 0.15, 0.25, 0.35, 0.45))
gnp_data$p <- factor(gnp_data$p)

pd <- position_dodge(0.6)
ggplot(gnp_data) +
    geom_bar(aes(x=p, y=value, fill=algorithm),
            position = pd, stat = "summary", fun.y = "mean", alpha=0.3, width=0.6) +
    geom_point(aes(x=p, y=value, fill=algorithm, color=algorithm),
               position=pd, size=0.5) +
    facet_wrap(~ N, labeller=label_both) +
    theme_bw() +
    ggtitle("Complexity measures of G(N,p) network")


pref_attach <- readr::read_tsv("compare_preferential_attach_data.txt")
pref_attach <- filter(pref_attach, seed_p %in% c(0.05, 0.15, 0.25, 0.35, 0.45))
pref_attach$seed_p <- NULL
pref_attach$seed_n_edge <- NULL
pref_attach$n_edge <- NULL
pref_attach <- gather(pref_attach, key="algorithm", value="value", -N, -m)
pref_attach$m <- factor(pref_attach$m)

pd <- position_dodge(0.6)
ggplot(pref_attach) +
    geom_bar(aes(x=m, y=value, fill=algorithm),
        position = pd, stat = "summary", fun.y = "mean", alpha=0.3, width=0.6) +
    geom_point(aes(x=m, y=value, fill=algorithm, color=algorithm),
        position = pd, size=0.5) +
    facet_wrap(~ N, labeller=label_both) +
    theme_bw() +
    ggtitle("Complexity measures of preferential attachment network")

pref_attach <- readr::read_tsv("compare_preferential_attach_data.txt")
pref_attach <- filter(pref_attach, seed_p %in% c(0.05, 0.15, 0.25, 0.35, 0.45))
pref_attach$seed_n_edge <- NULL
pref_attach$n_edge <- NULL
pref_attach <- rename(pref_attach, p = seed_p)
pref_attach <- gather(pref_attach, key="algorithm", value="value", -N, -m, -p)
pref_attach

gnp_data <- readr::read_tsv("compare_gnp_data.txt")
gnp_data <- tidyr::gather(gnp_data, key = "algorithm", value = "value", -N, -p)
gnp_data <- filter(gnp_data, p %in% c(0.05, 0.15, 0.25, 0.35, 0.45))
gnp_data <- filter(gnp_data, N==200)
gnp_data

stopifnot(all(gnp_data$N == pref_attach$N))
stopifnot(all(gnp_data$p == pref_attach$p))
stopifnot(all(gnp_data$algorithm == pref_attach$algorithm))

gnp_data$N <- NULL; gnp_data$p <- NULL; gnp_data$algorithm <- NULL

pref_attach <- rename(pref_attach, pref_attach = value)
gnp_data <- rename(gnp_data, gnp = value)

df <- cbind(pref_attach, gnp_data)
df <- tibble::as_tibble(df)

# remove topological info content
df <- filter(df, algorithm != "TopologicalInfoContent")

df <- df %>% group_by(N, p, m, algorithm) %>%
    summarize(p_value = t.test(gnp, pref_attach)$p.value,
              pref_attach_greater_than_gnp = mean(pref_attach) > mean(gnp))
arrange(df, algorithm, N, p)

