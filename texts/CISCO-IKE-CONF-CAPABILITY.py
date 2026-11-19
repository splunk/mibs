#
# PySNMP MIB module CISCO-IKE-CONF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IKE-CONF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCicIkeCfgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 489))
ciscoCicIkeCfgCapability.setRevisions(('2006-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoCicIkeCfgCapability.setDescription('Agent capabilities for\n                 CISCO-IKE-CONFIGURATION-MIB')
cCicIkeCfgCapSanOSV30R1MDS9000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 489, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCicIkeCfgCapSanOSV30R1MDS9000 = cCicIkeCfgCapSanOSV30R1MDS9000.setProductRelease('Cisco SanOS 3.0(1) on Cisco MDS 9000\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cCicIkeCfgCapSanOSV30R1MDS9000 = cCicIkeCfgCapSanOSV30R1MDS9000.setStatus('current')
if mibBuilder.loadTexts: cCicIkeCfgCapSanOSV30R1MDS9000.setDescription('Cisco IKE Configuration \n                     MIB capabilities')
mibBuilder.exportSymbols("CISCO-IKE-CONF-CAPABILITY", PYSNMP_MODULE_ID=ciscoCicIkeCfgCapability, cCicIkeCfgCapSanOSV30R1MDS9000=cCicIkeCfgCapSanOSV30R1MDS9000, ciscoCicIkeCfgCapability=ciscoCicIkeCfgCapability)
