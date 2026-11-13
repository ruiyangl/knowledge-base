# AI

Hardware / Compute Infrastructure Layer

### 🧱 1. **Hardware / Compute Infrastructure Layer**

*Provides the physical compute power for AI training and inference.*

- **Components**: GPUs, TPUs, ASICs, networking fabric, data centers
- **Key Players**: NVIDIA, AMD, Intel, TSMC, AWS (Inferentia/Trainium), Google (TPU), Microsoft Azure, Meta’s custom chips
- **valuation:**

---

### ⚙️ 2. **AI Infrastructure / Foundational Tools Layer**

*Enables the building, training, fine-tuning, and deployment of models.*

- **Sub-layers**:
    - **Model training frameworks**: PyTorch, TensorFlow, JAX
    - **MLOps tools**: Weights & Biases, MLflow, Kubeflow, Ray
    - **Vector DBs**: Pinecone, Weaviate, FAISS, Chroma
    - **Data pipelines & labeling**: Scale AI, Snorkel, Labelbox

---

### 🧠 3. **Foundation Models Layer (Model Providers)**

*Build and offer large general-purpose AI models.*

- **Key Players**:
    - **Open models**: Meta (Llama 3), Mistral, Hugging Face
    - **Closed/commercial**: OpenAI (GPT-4), Anthropic (Claude), Google DeepMind (Gemini), Cohere, xAI, AI21 Labs

---

### 🧩 4. **Middleware / API / Orchestration Layer**

*Connects models to applications, provides interfaces and orchestration.*

- **Functions**: API gateways, routing, memory management, prompt orchestration, agent frameworks
- **Key Players**: LangChain, LlamaIndex, Replit AI, Vercel AI SDK, Modal, Fixie, Dust, Semantic Kernel (Microsoft)

---

### 🛠️ 5. **Fine-tuning / Vertical Model Layer**

*Custom models built or adapted for specific industries, tasks, or data.*

- **Examples**:
    - **Healthcare**: Hippocratic AI, Tempus AI
    - **Legal**: Harvey AI, Casetext
    - **Financial**: BloombergGPT, FinGPT
    - **Code**: Code Llama, DeepSeek-Coder, Tabnine

---

### 💼 6. **Application / Product Layer**

*Consumer- or business-facing apps powered by AI models.*

- **Categories**:
    - **Productivity**: Notion AI, Grammarly, Jasper
    - **Coding**: GitHub Copilot, Replit Ghostwriter
    - **Search/Chat**: Perplexity, You.com, Arc Search
    - **Enterprise tools**: Salesforce Einstein, Microsoft Copilot, Adobe Firefly
    - **Agentic apps**: Devin (Cognition), MultiOn, AutoGPT (R&D)

---

### 📈 7. **Distribution & Integration Layer**

*How AI reaches end users and gets embedded in workflows.*

- **Channels**: Browsers, enterprise SaaS, APIs, embedded SDKs, marketplaces (AWS/GCP/Azure), CRM/ERP integrations
- **Examples**: Microsoft 365 + Copilot, Google Workspace + Gemini, Zoom + Otter.ai, SAP AI Core

### 🧱 **1. Hardware / Compute Infrastructure Layer**

| **Company** | **Status** | **Market Cap / Est. Valuation** | PE/Forward PE 2025 | PEG | **Description** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- |
| **NVIDIA** | **Public (NVDA)** | **~$3.45 T** | **45.72/29.23** | 1.01 | **NVIDIA is a computing infrastructure company focused on accelerating workloads like AI and graphics, providing chips, systems, and software for data centers and other markets.** | **Market cap based on most recent trading data on Google Finance.** |
| **AMD** | **Public (AMD)** | $188.39 B | **84.83/27.62** | **1.06** | **AMD is a high-performance and adaptive computing leader, powering products and services for data centers, embedded systems, gaming, and PCs with its CPUs, GPUs, and adaptive SoCs.** | **Market cap based on most recent trading data on Google Finance.** |
| **Intel** | **Public (INTC)** | $87.50 B | n/a/89.35 | n/a  | **Intel is a leading semiconductor company that designs and manufactures a wide range of processors and technologies for computers, servers, and other electronic devices.** | A18 reception was not stella and it need it to excel to tern around. Def too early  |
| **Broadcom** | **Public (AVGO)** | $1.16 T | 90.04/33.97 | 1.47 | **Broadcom is a global infrastructure technology leader providing semiconductor and infrastructure software solutions for data centers, networking, broadband, wireless, and industrial markets.** | **Market cap based on most recent trading data on Google Finance.** |
| **Arista Networks** | **Public** | $122.14B | **41.04/37.62** | **1.89** | **Arista Networks is an industry leader in data-driven cloud networking, designing and selling network switches and software for large data center, cloud computing, and high-performance environments.** | **Market cap based on most recent trading data on Google Finance.** |
| **Marvell Technology** | **Public** | $58.93 B | **n/a/23.03** | **0.50** | **Marvell Technology is a global leader in providing data infrastructure technology, specializing in semiconductor solutions for areas like networking, storage, and connectivity.** | **Market cap based on most recent trading data on Google Finance.** |
| **Cisco** | **Public (CSCO)** | $261.60 B | 26.98/16.76 | 3.62 | **Cisco is a worldwide leader in networking equipment and software, providing solutions for enterprise, service provider, and small business markets, including routing, switching, security, and collaboration products.** | **Market cap based on most recent trading data on Google Finance.** |
| **TSMC** | **Public (TSM)** | $860.47 B | 21.87/16.21 | n/a  | **TSMC is the world's largest dedicated semiconductor foundry, specializing in the manufacturing of chips designed by other companies for a wide range of applications.** | **Market cap based on most recent trading data on Google Finance.** |
| **Microsoft** | **Public (MSFT)** | **~$3.44 T** | 36.35/32.63 | 2.68  | **Microsoft is a global technology company that develops and supports software, services, devices, and solutions, including cloud computing, operating systems, productivity applications, and gaming.** | **Market cap based on most recent trading data on Google Finance.** |
| **Google (Alphabet)** | **Public (GOOGL)** | **~$1.90 T** | 19.38/18.85 | 1.26   | **Alphabet is a multinational technology conglomerate specializing in Internet-related services and products, including search, advertising, cloud computing, software, and hardware.** | **Market cap based on most recent trading data on Google Finance.** |
| **Amazon** | **Public (AMZN)** | $2.27 T | 34.80/33.86 | 1.97   | **Amazon is an e-commerce and cloud computing giant, offering a wide range of products and services including online retail, digital streaming, artificial intelligence, and cloud infrastructure through AWS.** | **Market cap based on most recent trading data on Google Finance.** |
| **Meta** | **Public (META)** | $1.75 T | 27.27/27.51 | 1.52 | **Meta is a technology company focused on social media platforms like Facebook, Instagram, and WhatsApp, and increasingly investing in the metaverse.** | **Market cap based on most recent trading data on Google Finance.** |
| **Groq** | **Private** | **~$3.14B** |  |  | **Groq is an AI chip startup specializing in fast AI responses, developing hardware and software for high-speed inference.** | **Valuation from a funding round led by Cisco Investments, Samsung Catalyst Fund, and BlackRock Private Equity Partners in August 2024.** |
| **Cerebras** | **Private** | **~$8.58B** |  |  | **Cerebras Systems is an AI company building powerful wafer-scale processors and systems for accelerating AI and deep learning workloads.** | **Implied valuation as of February 10, 2025; known for its Wafer-Scale Engine (WSE) per PM Insights.** |
| **SambaNova** | **Private** | **~$2.13B** |  |  | **SambaNova Systems is an AI chip startup offering DataScale and Dataflow-as-a-Service platforms for accelerating AI training and inference.** | **Implied valuation as of February 10, 2025; offers DataScale and Dataflow-as-a-Service platforms per PM Insights.** |
| **Graphcore** | **Private** | ***Acquired by SoftBank*** |  |  | **Graphcore is an AI chip company that develops Intelligence Processing Units (IPUs) designed for machine learning workloads.** | **Acquired by SoftBank in July 2024; last known valuation was $2.8B according to EE Times.** |
| **Tenstorrent** | **Private** | **~$2.6 B** |  |  | **Tenstorrent is an AI chip startup focused on RISC-V and developing hardware and software for AI acceleration.** | **AI chip startup backed by Jeff Bezos and Samsung according to Fortune.** |
| **Etched** | **Private** | **~$302.85M** |  |  | **Etched is an AI chip startup developing specialized hardware for transformer models, aiming to accelerate AI workloads efficiently.** | **AI chip startup developing a transformer-specialized chip per Hiive.** |
| **Hailo** | **Private** | **n/a** |  |  | **Hailo is an AI chip company that focuses on developing AI processors specifically for edge devices and AI applications.** | **AI chip startup focused on edge AI processing.** |
| **Cornelis Networks** | **Private** | **n/a** |  |  | **Cornelis Networks provides high-performance interconnect solutions for high-performance computing (HPC) and AI workloads.** | **Provider of high-performance interconnects for HPC, AI, and ML.** |
| Nebius  | Public (NBIS) |  |  |  |  |  |
| Navitas  | Public (NVTS) |  |  |  |  |  |

---

### ⚙️ **2. AI Infrastructure / Foundational Tools Layer**

| **Company** | **Status** | **Market Cap / Est. Valuation** | PE/Forward PE 2025 | PEG | **Description** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- |
| Synopsys  | **Public**(SNPS) | **~$75.41B** | 56.18/29.99 | 2.18 | **Synopsys is a leading provider of electronic design automation (EDA) software and services used for designing and verifying integrated circuits and electronic systems.** | **Market cap as of June 6, 2025, according to [Stock Analysis](https://stockanalysis.com/stocks/snps/market-cap/) and [Morningstar](https://www.morningstar.com/stocks/xnas/snps/quote).** |
| **Arteris** | **Public (NASDAQ: AIP)** | $332.9 M | n/a/n/a | n/a | **Arteris offers network-on-chip (NoC) interconnect IP for complex SoCs, helping design high-performance, low-power systems.** | **Market cap as of February 24, 2025.** |
| **AWS** | **Public (AMZN)** | **~$2.02 T** |  |  | **AWS, Amazon Web Services, is the world's most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally.** | **AWS is a segment of Amazon.com, Inc. The total market cap of Amazon is ~$2.02T. AWS accounts for a significant portion of Amazon's operating profits. As of Q2 FY2024, AWS accounted for 15% of Amazon's total revenue and 50% of its operating income.** |
| **Google Cloud** | **Public (GOOGL)** | **~$1.90 T** |  |  | **Google Cloud Platform (GCP) is Google's suite of cloud computing services, providing infrastructure and software for a wide range of applications, including AI and machine learning.** | **Google Cloud is a segment of Alphabet Inc. The total market cap of Alphabet is ~$1.90T.** |
| **Microsoft Azure** | **Public (MSFT)** | **~$3.44 T** |  |  | **Microsoft Azure is a growing cloud computing platform offering a broad range of services, including compute, analytics, storage, and networking.** | **Microsoft Azure is a segment of Microsoft. The total market cap of Microsoft is ~$3.44T.** |
| **CoreWeave** | **Private** | **$67.27B** | n/a/n/a | n/a | **CoreWeave is a cloud provider specializing in high-performance computing, particularly for AI and machine learning workloads.** | **CoreWeave's valuation was estimated at $19 billion as of May 23, 2025.** |

---

### 🧠 **3. Foundation Models Layer**

| **Company** | **Status** | **Market Cap / Est. Valuation** | PE/Forward PE 2025 | PEG | **Description** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- |
| **OpenAI** | **Private** | **~$300 B** |  |  | **OpenAI is an AI research and deployment company focused on developing advanced artificial intelligence with the goal of benefiting all of humanity.** |  |
| **Anthropic** | **Private** | **~$61.5 B** |  |  | **Anthropic is an AI safety and research company that develops large language models like Claude, prioritizing ethical AI development and responsible deployment.** | **Anthropic's valuation reached $61.5 billion after its Series E funding round in February 2025.** |
| **Google DeepMind** | **Private (subsidiary)** | **part of Alphabet** |  |  | **Google DeepMind is Google's AI research lab, working on advanced AI technologies and systems, contributing to Google's products and services.** | **Google DeepMind is a division within Alphabet (GOOGL), which has a market cap of ~$1.90T.** |
| **Meta (LLaMA)** | **Internal division** | **—** |  |  | **Meta develops large language models like LLaMA as part of its internal AI research and development efforts, with the aim of advancing AI capabilities for its various platforms.** | **This is an internal research project or division within Meta (META), which has a market cap of ~$1.46T. It's not a separate entity with its own market cap.** |
| **Hugging Face** | **Private** | **~$4.5 B** |  |  | **Hugging Face is a platform providing tools and resources for building, training, and deploying machine learning models, particularly large language models.** | **Hugging Face's most recent valuation is $4.5 billion, based on a Series D funding round in 2023.** |
| **Mistral AI** | **Private** | **~$6.2B** |  |  | **Mistral AI is a European AI company focused on developing large language models and generative AI technologies, aiming to be a leader in the field.** | **Mistral AI's valuation was recently reported to be around $6.2 billion in a funding round as of June 2024.** |
| **Cohere** | **Private** | **~$5.5 B** |  |  | **Cohere is an AI company focused on building large language models for enterprise applications, providing secure and cloud-agnostic solutions for businesses.** | **Cohere has a valuation of $5.5 billion after its Series D round in July 2024.** |
| **xAI** | **Private** | **~$113 B** |  |  | **xAI is an artificial intelligence company founded by Elon Musk, focused on understanding the true nature of the universe and developing AI that is aligned with humanity.** | **xAI's valuation was reportedly $113 billion in a recent funding round.** |
| **Cerebras** | **Private** | **~$4.72B** |  |  | **Cerebras Systems develops AI-specific hardware, including the Wafer-Scale Engine (WSE), designed for accelerating massive AI computations and training large language models.** | **The Forge Price valuation for Cerebras is $4.72B as of June 8, 2025. The company filed for an IPO in September 2024, aiming for a valuation between $7 billion and $8 billion. Their most recent private valuation was $4 billion in November 2021.** |

---

### 🧬 **4. Fine-tuning / Vertical Model Layer**

| **Company** | **Status** | **Market Cap / Est. Valuation** | PE/Forward PE 2025 | PEG | **Description** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- |
| **BloombergGPT** | **Private** | **n/a** |  |  | **BloombergGPT is a large language model developed by Bloomberg specifically for the financial industry, trained on extensive financial data.** |  |
| **Tempus AI** | **Private** | $10.75B | n/a/n/a | n/a | **Tempus AI is a precision medicine company leveraging AI to analyze clinical and molecular data for personalized patient care.** | **Tempus was reportedly targeting a valuation around $5 billion for a funding round in April 2024.** |
| **Aleph Alpha** | **Private** | **~$500M** |  |  | **Aleph Alpha is a German AI company developing large language models and multimodal AI solutions, focusing on explainable AI and trusted applications.** | **Aleph Alpha was valued at around €500 million ($540 million USD) after a Series B funding round in November 2023.** |
| **IBM Granite** | **Private (subsidiary)** | **part of IBM (~$150 B)** |  |  | **IBM Granite is a family of enterprise-focused generative AI models designed for various business applications, including language and code generation, prioritizing trust, safety, and scalability.** | **IBM Granite models are available on platforms like Hugging Face under the Apache 2.0 open-source license.** |
| **Bloomberg** | **Private** | **~$120B** |  |  | **Bloomberg L.P. is a privately held financial, software, data, and media company known for its Bloomberg Terminal financial data and analysis platform.** | **The exact valuation of a privately held company like Bloomberg can be difficult to determine, but it's estimated to be around $120 billion.** |
| **Abridge** | **Private** | **~$2.75B** |  |  | **Abridge is an AI-powered platform designed to reduce clinical documentation burden for healthcare providers by converting patient-clinician conversations into structured clinical notes.** | **Abridge reached a post-money valuation of $2.75 billion after a Series D funding round in February 2025.** |
| **Harvey** | **Private** | **~$2B** |  |  | **Harvey is an AI platform specifically developed for the legal profession, providing tools and support for tasks like contract analysis, due diligence, and legal research.** | **Harvey was recently targeting a valuation of $2 billion for a new funding round.** |
| **Vannevar Labs** | **Private** | **~$575M** |  |  | **Vannevar Labs is a defense technology startup that provides software and hardware solutions to address critical national security challenges, focusing on advanced data analysis and intelligence gathering.** | **Vannevar Labs was valued at $575 million after its Series B funding round in January 2023.** |
| **Jasper** | **Private** | **~$1.5B** |  |  | **Jasper is a generative AI platform for content creation, helping marketing teams and businesses generate marketing copy, blog posts, and other content.** | **Jasper was last valued at $1.5 billion in its Series B funding round in October 2022.** |
| **Writer.com** | **Private** | **~$1.9B** |  |  | **Writer.com is an AI writing assistant and content creation platform designed for enterprise teams, providing tools to ensure brand voice consistency and generate high-quality content.** | **Writer.com secured $100 million in a Series B funding round in September 2023, bringing its total valuation to $1.9 billion.** |
| **Cerebras** | **Private** | **~$4.72B** |  |  | **Cerebras Systems develops AI-specific hardware, including the Wafer-Scale Engine (WSE), designed for accelerating massive AI computations and training large language models.** | **The Forge Price valuation for Cerebras is $4.72B as of June 8, 2025. The company filed for an IPO in September 2024, aiming for a valuation between $7 billion and $8 billion. Their most recent private valuation was $4 billion in November 2021.** |

---

### 💻 **5. Application / Product Layer**

| **Company/Product** | **Status** | **Market Cap / Est. Valuation** | PE/Forward PE 2025 | PEG | **Description** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- |
| **ChatGPT (OpenAI)** | **Private** | **under OpenAI** |  |  | **ChatGPT is a large language model developed by OpenAI, designed to engage in conversational AI and generate human-like text responses across various prompts and topics.** | **ChatGPT is a product developed and owned by OpenAI, a private company valued at approximately $300B.** |
| **Claude (Anthropic)** | **Private** | **under Anthropic** |  |  | **Claude is a large language model created by Anthropic, focused on providing helpful, honest, and harmless responses, aiming to ensure AI safety and trustworthiness.** | **Claude is a product developed and owned by Anthropic, a private company valued at approximately $61.5B.** |
| **Gemini (Google)** | **Private (subdiv.)** | **part of Alphabet** |  |  | **Gemini is a family of multimodal AI models developed by Google, capable of processing and generating various types of information, including text, images, audio, video, and code, aiming to provide advanced AI capabilities across different applications.** | **Gemini is a product developed within Google, a subsidiary of Alphabet Inc., which has a market cap of approximately $1.90T.** |
| **Microsoft Copilot** | **Public (MSFT)** | **part of Microsoft** |  |  | **Microsoft Copilot is a suite of AI-powered features designed to enhance productivity and creativity across various Microsoft applications, like Microsoft 365 and Windows, by providing intelligent assistance and personalized support.** | **Microsoft Copilot is a product developed by Microsoft, which has a market cap of approximately $3.44T.** |
| **Notion AI** | **Private** | **n/a** |  |  | **Notion AI is a suite of AI-powered features integrated into the Notion workspace, designed to improve various workflows like content generation, brainstorming, and writing assistance, aiming to enhance productivity and creativity for users.** |  |
| **GitHub Copilot** | **Public (MSFT)** | **part of Microsoft** |  |  | **GitHub Copilot is an AI-powered code completion tool designed to assist software developers by suggesting code snippets and lines based on the context of the code being written, aiming to improve efficiency and reduce coding time.** | **GitHub Copilot is a product developed by Microsoft, which has a market cap of approximately $3.44T.** |
| **Midjourney** | **Private** | **n/a** |  |  | **Midjourney is an AI art generator platform that creates unique images from textual descriptions, providing a tool for artists and individuals to explore visual creations and generate art using artificial intelligence.** |  |
| **HeyGen** | **Private** | **n/a** |  |  | **HeyGen is an AI video generation platform that helps users create professional-quality videos using text-to-video capabilities, aiming to simplify the video production process for businesses and content creators.** |  |
| **RunwayML** | **Private** | **n/a** |  |  | **RunwayML is a video editing and content creation platform that combines AI and machine learning tools, enabling users to add unique effects and generate video content more efficiently.** |  |
| **ElevenLabs** | **Private** | **n/a** |  |  | **ElevenLabs is a voice synthesis and AI audio company that develops advanced AI-powered text-to-speech technology, providing tools for creating high-quality, realistic voices for various applications.** |  |

---

### 📦 **6. Distribution & Integration Layer**

| **Salesforce Einstein** | **Public (CRM)** | **~$200 B** | PE/Forward PE 2025 | PEG | **Salesforce Einstein integrates AI technologies into the Salesforce customer relationship management (CRM) platform, providing predictive analytics, recommendations, and automation across sales, service, and marketing functions.** | **The market cap reflects the parent company, Salesforce (CRM), which has a market cap of approximately $200B.** |
| --- | --- | --- | --- | --- | --- | --- |
| **Microsoft 365 Copilot** | **Public (MSFT)** | **part of Microsoft** |  |  | **Microsoft 365 Copilot is an AI-powered assistant within Microsoft 365 applications, offering AI assistance for tasks like writing, data analysis, and email drafting.** | **Microsoft 365 Copilot is a product developed by Microsoft, which has a market cap of approximately $3.44T.** |
| **Google Workspace AI tools** | **Public (GOOGL)** | **part of Alphabet** |  |  | **Google Workspace AI tools, including Gemini, enhance productivity and creativity within Google Workspace applications by providing AI-powered assistance for tasks like writing, summarizing, and data analysis.** | **These AI tools are part of Google Workspace, a product developed by Google, a subsidiary of Alphabet Inc., which has a market cap of approximately $1.90T.** |
| **Zoom AI Companion** | **Public (ZM)** | **~$20 B** |  |  | **Zoom AI Companion provides AI features within Zoom's video conferencing platform, such as meeting summaries, smart recording, and chat summaries, designed to enhance meeting productivity.** | **The market cap reflects the parent company, Zoom Video Communications (ZM), which has a market cap of approximately $22B.** |
| **Slack GPT** | **Public (MSFT)** | **part of Microsoft** |  |  | **Slack GPT integrates OpenAI's ChatGPT into the Slack communication platform, enabling users to interact with the AI model for tasks like asking questions, summarizing conversations, and drafting messages within Slack.** | **Slack is a product of Salesforce, which has a market cap of approximately $200B.** |
| **SAP Joule** | **Public (SAP)** | **~$175 B** |  |  | **SAP Joule is a generative AI assistant integrated into SAP's business applications, designed to help users with tasks such as accessing information, automating workflows, and completing tasks across different SAP modules.** | **The market cap reflects the parent company, SAP (SAP), which has a market cap of approximately $175B.** |
| **Zapier** | **Private** | **~$5B** |  |  | **Zapier is a no-code automation platform that connects various web applications to automate workflows and tasks, allowing users to create automated processes without requiring coding knowledge.** | **Zapier was valued at $5 billion after its Series D funding round in January 2022.** |
| **Make.com** | **Private** | **part of Celonis** |  |  | **Make.com (formerly Integromat) is a visual platform that allows users to design, build, and automate complex workflows by connecting different apps and services using a visual interface.** | **Make.com is a part of Celonis, a process mining and execution management software company valued at $13 billion.** |
| **UiPath** | **Public (PATH)** | **~$7.06B** | n/a/**23.60** | **2.70** | **UiPath is a leading robotic process automation (RPA) software company that develops software robots to automate repetitive tasks and workflows for businesses, helping to improve efficiency and productivity.** | **The market cap reflects the parent company, UiPath (PATH), which has a market cap of approximately $7.06B as of June 6, 2025.** |
| **Automation Anywhere** | **Private** | **~$6.8B** |  |  | **Automation Anywhere is a global leader in robotic process automation (RPA), providing a platform to automate business processes and workflows using software bots.** | **Automation Anywhere's valuation was estimated at $6.8 billion after its Series B funding round in November 2021.** |
| **Twilio** | **Public (TWLO)** | **~$15 B** | n/a/**25.90** | **2.56** | **Twilio is a cloud communications platform that enables developers to embed messaging, voice, and video into applications, providing APIs for building various communication solutions.** | **The market cap reflects the parent company, Twilio (TWLO), which has a market cap of approximately $15B.** |
| **Gigs** | **Private** | **~$73M** |  |  | **Gigs is a platform that allows tech companies to embed mobile services into their products and services, enabling them to offer mobile connectivity as a feature to their customers.** | **Gigs raised $73 million in a Series B funding round in December 2024, at which point its valuation was not publicly disclosed, but this funding level suggests a substantial valuation.** |

---