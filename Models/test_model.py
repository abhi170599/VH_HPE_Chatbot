import pickle 

file = open('data_6.pickle','rb')

data = pickle.load(file)

question_dict = data['question_dict']


answer_file = open('answers.pickle','rb')
answer_list = pickle.load(answer_file)

print(len(answer_list['answers']))

answers_dict = {

           5: "HPE OneView provides a wide variety of capabilities for managing converged infrastructure, including: onverged management architecture for HPE servers, storage, and network management (HPE Virtual Connect and select third-party switch platforms)• Software-defined control (profiles, templates, groups, and sets)• Open integration using the REST API and state-change message bus • Automated storage provisioning • HPE Virtual Connect (VC) management • Pervasive Smart Search and MapView • Remote management with HPE Integrated Lights Out (iLO)Frequently asked questions Page 5 • Environmental (power and thermal) management • System health monitoring • Firmware compliance management and updates • Integrated Remote Support • HPE Remote Technician for remote troubleshooting • Server provisioning • Cluster provisioning and rolling updates for VMware vSphere® • Security • Appliance backups • VMware® integrations • Microsoft® integrations • Web-based training to basic product proficiency • Three years of Technical Support and Updates (TS&U) These capabilities deliver converged management that reduces infrastructure complexity with automation simplicity. It’s a modern, integrated workspace for IT team collaboration, which automates the deployment and management of infrastructure repeatedly, reliably, and at scale.",
           6: "The HPE OneView management appliance controls licenses. The same management appliance can be used for both HPE OneView Advanced licenses and for HPE OneView Standard. This choice is made by the user when they initially add their system to the HPE OneView management appliance.• HPE OneView Advanced provides full-featured licenses, which can be purchased for managing Gen8, Gen9 and Gen10 servers. All HPE OneView Advanced versions are licensed “per physical server.” These licenses include three years of 24x7 Technical Support and Updates (TS&U) and access to introductory one-hour web-based training (WBT) providing an overview.• There are two types of HPE OneView licenses: – HPE OneView with iLO Advanced – HPE OneView without iLO Advanced • HPE OneView Standard can be used for inventory, health monitoring, alerting, and reporting without additional fees. HPE OneView Standard can monitor Gen6, Gen7, Gen8, Gen9, and Gen10 servers. The user interface is similar to the HPE OneView Advanced version, but the software-defined functionality is not available. Once deployed, both storage and servers are monitored in HPE OneView, and the storage topology is viewable in MapView. It doesn’t include Support and Updates. An annual 9x5 Support and Updates offering is available for additional fee with SKU K6F98AAE.• The HPE OneView management appliance controls the licenses, and it can be obtained in two ways: – Software download Virtual Machine Appliance(VMA) from HPE Software Depot – Purchase of the HPE OneView Media Kit (contains a USB flash drive) Please note that the HPE OneView licenses after applied to server(s) are not transferrable. HPE OneView Advanced management software can be used for 60 days without charge. This is a trial period, and after 60 days, customers must apply HPE OneView licenses.",
          43: "HPE OneView for VMware vCenter, vRealize® Operations ManagerTM and VMware vRealize® Log InsightTM seamlessly integrates the manageability features of HPE Synergy, ProLiant, BladeSystem, Virtual Connect, and Storage with VMware solutions. This provides deep insight and control of virtualized HPE Converged Infrastructure environments while reducing the time it takes to make important changes,increasing capacity or manage planned and unplanned downtime. VMware vCenter Operations Manager and Log Insight integrations deliver powerful analytics and deeper troubleshooting tools to your VMware administrators. HPE OneView for VMware vRealize® OrchestratorTM or helps customers automate complex IT tasks in an extensible and repeatable manner. It provides a predefined collection of HPE tasks and workflows that can be used in vRealize Orchestrator (VRO), with easy-to-use, drag and drop access to automation of HPE OneView managed hardware deployment, firmware updates, and other lifecycle tasks. HPE OneView for VMware vRealize Orchestrator allows the advanced management features of HPE OneView to be incorporated into larger IT workflows. HPE OneView workflows and actions can also be integrated in VMware vRealize® AutomationTM via vRealize Orchestrator. More information can be found at hpe.com/products/ovvcenter."
}

answer_list['answers'].insert(5,answers_dict[5])
answer_list['answers'].insert(6,answers_dict[6])
answer_list['answers'].insert(43,answers_dict[43])


print(len(answer_list['answers']))

answer_file_updated = open('answers_updated.pickle','wb')
pickle.dump(answer_list,answer_file_updated)

"""
for pair in question_dict['server']:

    print(pair['answer'])
    print("\n")
"""