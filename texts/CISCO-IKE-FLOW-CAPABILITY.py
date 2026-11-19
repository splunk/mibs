#
# PySNMP MIB module CISCO-IKE-FLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IKE-FLOW-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIkeFlowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 487))
ciscoIkeFlowCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIkeFlowCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoIkeFlowCapability.setDescription('Agent capabilities for\n                 CISCO-IKE-FLOW-MIB.')
ciscoIkeFlowCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 487, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIkeFlowCapSanOSV30R1MDS9000 = ciscoIkeFlowCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000 \n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIkeFlowCapSanOSV30R1MDS9000 = ciscoIkeFlowCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: ciscoIkeFlowCapSanOSV30R1MDS9000.setDescription('Cisco IKE Flow Monitoring\n                     MIB capabilities')
mibBuilder.exportSymbols("CISCO-IKE-FLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoIkeFlowCapability, ciscoIkeFlowCapSanOSV30R1MDS9000=ciscoIkeFlowCapSanOSV30R1MDS9000, ciscoIkeFlowCapability=ciscoIkeFlowCapability)
