#
# PySNMP MIB module CISCO-ITP-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-MONITOR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
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
ciscoItpMonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 422))
ciscoItpMonCapability.setRevisions(('2004-11-23 00:00', '2004-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpMonCapability.setRevisionsDescriptions(('Add the new ciscoItpmNotificationsGroupRev1 group\n                to support ciscoItpMonitorState notification.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpMonCapability.setLastUpdated('200411230000Z')
if mibBuilder.loadTexts: ciscoItpMonCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpMonCapability.setContactInfo('       Cisco Systems\n                       Customer Service\n               \n               Postal: 170 West Tasman Drive\n                       San Jose, CA  95134\n                       USA\n               \n                  Tel: +1 800 553-NETS\n               \n               E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpMonCapability.setDescription('Agent capabilities for the CISCO-ITP-MONITOR-MIB.')
ciscoItpMonCapabilityV12R0221SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 422, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0221SW = ciscoItpMonCapabilityV12R0221SW.setProductRelease('Cisco IOS 12.2(21)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0221SW = ciscoItpMonCapabilityV12R0221SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMonCapabilityV12R0221SW.setDescription('IOS 12.2(21)SW Cisco CISCO-ITP-MONITOR-MIB.my \n                     User Agent MIB capabilities.')
ciscoItpMonCapabilityV12R0251SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 422, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0251SW = ciscoItpMonCapabilityV12R0251SW.setProductRelease('Cisco IOS 12.2(25)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpMonCapabilityV12R0251SW = ciscoItpMonCapabilityV12R0251SW.setStatus('current')
if mibBuilder.loadTexts: ciscoItpMonCapabilityV12R0251SW.setDescription('IOS 12.2(25)SW Cisco CISCO-ITP-MONITOR-MIB.my \n                     User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-MONITOR-CAPABILITY", ciscoItpMonCapabilityV12R0221SW=ciscoItpMonCapabilityV12R0221SW, ciscoItpMonCapabilityV12R0251SW=ciscoItpMonCapabilityV12R0251SW, PYSNMP_MODULE_ID=ciscoItpMonCapability, ciscoItpMonCapability=ciscoItpMonCapability)
