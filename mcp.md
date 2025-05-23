Notes on Model Context Protocol (MCP)


Importance of MCP
The AI ecosystem is evolving rapidly, with Large Language Models (LLMs) and other AI systems becoming increasingly capable. However, these models are often limited by their training data and lack access to real-time information or specialized tools. This limitation hinders the potential of AI systems to provide truly relevant, accurate, and helpful responses in many scenarios.

This is where Model Context Protocol (MCP) comes in. MCP enables AI models to connect with external data sources, tools, and environments, allowing for the seamless transfer of information and capabilities between AI systems and the broader digital world. This interoperability is crucial for the growth and adoption of truly useful AI applications.

Overview of Unit 1
Here’s a brief overview of what we’ll cover in this unit:

What is Model Context Protocol? - We’ll start by defining what MCP is and discussing its role in the AI ecosystem.
Key Concepts - We’ll explore the fundamental concepts and terminology associated with MCP.
Integration Challenges - We’ll examine the problems that MCP aims to solve, particularly the “M×N Integration Problem.”
Benefits and Goals - We’ll discuss the key benefits and goals of MCP, including standardization, enhanced AI capabilities, and interoperability.
Simple Example - Finally, we’ll walk through a simple example of MCP integration to see how it works in practice.


Key Concepts and Terminology
Before diving deeper into the Model Context Protocol, it’s important to understand the key concepts and terminology that form the foundation of MCP. This section will introduce the fundamental ideas that underpin the protocol and provide a common vocabulary for discussing MCP implementations throughout the course.

MCP is often described as the “USB-C for AI applications.” Just as USB-C provides a standardized physical and logical interface for connecting various peripherals to computing devices, MCP offers a consistent protocol for linking AI models to external capabilities. This standardization benefits the entire ecosystem:

users enjoy simpler and more consistent experiences across AI applications
AI application developers gain easy integration with a growing ecosystem of tools and data sources
tool and data providers need only create a single implementation that works with multiple AI applications
the broader ecosystem benefits from increased interoperability, innovation, and reduced fragmentation
The Integration Problem
The M×N Integration Problem refers to the challenge of connecting M different AI applications to N different external tools or data sources without a standardized approach.

Without MCP (M×N Problem)
Without a protocol like MCP, developers would need to create M×N custom integrations—one for each possible pairing of an AI application with an external capability.

Without MCP

Each AI application would need to integrate with each tool/data source individually. This is a very complex and expensive process which introduces a lot of friction for developers, and high maintenance costs.

Once we have multiple models and multiple tools, the number of integrations becomes too large to manage, each with its own unique interface.

Multiple Models and Tools

With MCP (M+N Solution)
MCP transforms this into an M+N problem by providing a standard interface: each AI application implements the client side of MCP once, and each tool/data source implements the server side once. This dramatically reduces integration complexity and maintenance burden.

With MCP

Each AI application implements the client side of MCP once, and each tool/data source implements the server side once.

Core MCP Terminology
Now that we understand the problem that MCP solves, let’s dive into the core terminology and concepts that make up the MCP protocol.

MCP is a standard like HTTP or USB-C, and is a protocol for connecting AI applications to external tools and data sources. Therefore, using standard terminology is crucial to making the MCP work effectively.

When documenting our applications and communicating with the community, we should use the following terminology.

Components
Just like client server relationships in HTTP, MCP has a client and a server.

MCP Components

Host: The user-facing AI application that end-users interact with directly. Examples include Anthropic’s Claude Desktop, AI-enhanced IDEs like Cursor, inference libraries like Hugging Face Python SDK, or custom applications built in libraries like LangChain or smolagents. Hosts initiate connections to MCP Servers and orchestrate the overall flow between user requests, LLM processing, and external tools.

Client: A component within the host application that manages communication with a specific MCP Server. Each Client maintains a 1:1 connection with a single Server, handling the protocol-level details of MCP communication and acting as an intermediary between the Host’s logic and the external Server.

Server: An external program or service that exposes capabilities (Tools, Resources, Prompts) via the MCP protocol.

A lot of content uses ‘Client’ and ‘Host’ interchangeably. Technically speaking, the host is the user-facing application, and the client is the component within the host application that manages communication with a specific MCP Server.

Capabilities
Of course, your application’s value is the sum of the capabilities it offers. So the capabilities are the most important part of your application. MCP’s can connect with any software service, but there are some common capabilities that are used for many AI applications.

Capability	Description	Example
Tools	Executable functions that the AI model can invoke to perform actions or retrieve computed data. Typically relating to the use case of the application.	A tool for a weather application might be a function that returns the weather in a specific location.
Resources	Read-only data sources that provide context without significant computation.	A researcher assistant might have a resource for scientific papers.
Prompts	Pre-defined templates or workflows that guide interactions between users, AI models, and the available capabilities.	A summarization prompt.
Sampling	Server-initiated requests for the Client/Host to perform LLM interactions, enabling recursive actions where the LLM can review generated content and make further decisions.	A writing application reviewing its own output and decides to refine it further.
In the following diagram, we can see the collective capabilities applied to a use case for a code agent.

collective diagram

This application might use their MCP entities in the following way:

Entity	Name	Description
Tool	Code Interpreter	A tool that can execute code that the LLM writes.
Resource	Documentation	A resource that contains the documentation of the application.
Prompt	Code Style	A prompt that guides the LLM to generate code.
Sampling	Code Review	A sampling that allows the LLM to review the code and make further decisions.

Architectural Components of MCP
In the previous section, we discussed the key concepts and terminology of MCP. Now, let’s dive deeper into the architectural components that make up the MCP ecosystem.

Host, Client, and Server
The Model Context Protocol (MCP) is built on a client-server architecture that enables structured communication between AI models and external systems.

MCP Architecture

The MCP architecture consists of three primary components, each with well-defined roles and responsibilities: Host, Client, and Server. We touched on these in the previous section, but let’s dive deeper into each component and their responsibilities.

Host
The Host is the user-facing AI application that end-users interact with directly.

Examples include:

AI Chat apps like OpenAI ChatGPT or Anthropic’s Claude Desktop
AI-enhanced IDEs like Cursor, or integrations to tools like Continue.dev
Custom AI agents and applications built in libraries like LangChain or smolagents
The Host’s responsibilities include:

Managing user interactions and permissions
Initiating connections to MCP Servers via MCP Clients
Orchestrating the overall flow between user requests, LLM processing, and external tools
Rendering results back to users in a coherent format
In most cases, users will select their host application based on their needs and preferences. For example, a developer may choose Cursor for its powerful code editing capabilities, while domain experts may use custom applications built in smolagents.

Client
The Client is a component within the Host application that manages communication with a specific MCP Server. Key characteristics include:

Each Client maintains a 1:1 connection with a single Server
Handles the protocol-level details of MCP communication
Acts as the intermediary between the Host’s logic and the external Server
Server
The Server is an external program or service that exposes capabilities to AI models via the MCP protocol. Servers:

Provide access to specific external tools, data sources, or services
Act as lightweight wrappers around existing functionality
Can run locally (on the same machine as the Host) or remotely (over a network)
Expose their capabilities in a standardized format that Clients can discover and use
Communication Flow
Let’s examine how these components interact in a typical MCP workflow:

In the next section, we’ll dive deeper into the communication protocol that enables these components with practical examples.

User Interaction: The user interacts with the Host application, expressing an intent or query.

Host Processing: The Host processes the user’s input, potentially using an LLM to understand the request and determine which external capabilities might be needed.

Client Connection: The Host directs its Client component to connect to the appropriate Server(s).

Capability Discovery: The Client queries the Server to discover what capabilities (Tools, Resources, Prompts) it offers.

Capability Invocation: Based on the user’s needs or the LLM’s determination, the Host instructs the Client to invoke specific capabilities from the Server.

Server Execution: The Server executes the requested functionality and returns results to the Client.

Result Integration: The Client relays these results back to the Host, which incorporates them into the context for the LLM or presents them directly to the user.

A key advantage of this architecture is its modularity. A single Host can connect to multiple Servers simultaneously via different Clients. New Servers can be added to the ecosystem without requiring changes to existing Hosts. Capabilities can be easily composed across different Servers.

As we discussed in the previous section, this modularity transforms the traditional M×N integration problem (M AI applications connecting to N tools/services) into a more manageable M+N problem, where each Host and Server needs to implement the MCP standard only once.

The architecture might appear simple, but its power lies in the standardization of the communication protocol and the clear separation of responsibilities between components. This design allows for a cohesive ecosystem where AI models can seamlessly connect with an ever-growing array of external tools and data sources.

Conclusion
These interaction patterns are guided by several key principles that shape the design and evolution of MCP. The protocol emphasizes standardization by providing a universal protocol for AI connectivity, while maintaining simplicity by keeping the core protocol straightforward yet enabling advanced features. Safety is prioritized by requiring explicit user approval for sensitive operations, and discoverability enables dynamic discovery of capabilities. The protocol is built with extensibility in mind, supporting evolution through versioning and capability negotiation, and ensures interoperability across different implementations and environments.

In the next section, we’ll explore the communication protocol that enables these components to work together effectively.



