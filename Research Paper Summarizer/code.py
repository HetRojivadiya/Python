from transformers import pipeline


def generate_summary(input_text):
    summarizer = pipeline("summarization")
    summary = summarizer(input_text, max_length=150,
                         min_length=50, do_sample=False)
    return summary[0]['summary_text'].strip()


def main():
    research_paper = """
Title: The Impact of Renewable Energy Sources on Sustainable Development
Abstract:The global energy landscape is undergoing a significant transformation with the increasing adoption of renewable energy sources. This research paper aims to analyze the impact of renewable energy sources on sustainable development. The paper reviews various studies on the environmental, economic, and social aspects of renewable energy integration.
Introduction:In recent years, the depletion of fossil fuels and growing concerns about climate change have prompted a shift towards renewable energy sources. This transition holds the potential to address both energy security and environmental challenges. However, the integration of renewable energy sources requires a comprehensive understanding of their impacts on sustainable development.
Environmental Impacts:Renewable energy sources such as solar, wind, hydroelectric, and geothermal power generate minimal greenhouse gas emissions compared to fossil fuels. This reduction in emissions contributes to mitigating the effects of climate change. Additionally, these sources have a lower environmental footprint in terms of land use and water consumption.
Economic Considerations:The adoption of renewable energy technologies has the potential to stimulate economic growth through job creation, technological innovation, and reduced energy costs. However, initial investments in infrastructure and technology can be substantial. Policymakers must balance these economic benefits with the short-term costs.
Social Benefits
Renewable energy projects often lead to localized benefits, including improved air quality, reduced health risks, and enhanced energy access in rural areas. Furthermore, community engagement and participation in energy projects can strengthen social cohesion and empowerment.
Challenges and Recommendations:Despite the numerous advantages, challenges such as intermittency, storage, and grid integration remain. Policymakers, researchers, and industry stakeholders must collaborate to address these challenges. Improved energy storage technologies and smart grid systems can enhance the reliability of renewable energy sources.
Conclusion:The integration of renewable energy sources into the energy mix holds significant promise for achieving sustainable development goals. However, a holistic approach is necessary to balance environmental, economic, and social considerations. Continued research and investment in renewable energy technologies will be essential for a cleaner and more sustainable energy future.
        """

    summary = generate_summary(research_paper)

    print("Original Research Paper:")
    print(research_paper)
    print("\nGenerated Summary:")
    print(summary)


if __name__ == "__main__":
    main()
