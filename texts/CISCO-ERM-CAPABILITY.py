#
# PySNMP MIB module CISCO-ERM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ERM-CAPABILITY
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
ciscoErmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 492))
ciscoErmCapability.setRevisions(('2006-03-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoErmCapability.setRevisionsDescriptions(('Initial version of the capability MIB for the ERM MIB module',))
if mibBuilder.loadTexts: ciscoErmCapability.setLastUpdated('200603090000Z')
if mibBuilder.loadTexts: ciscoErmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoErmCapability.setContactInfo('Cisco Systems\n                   Customer Service\n           Postal: 170 West Tasman Drive\n                   San Jose, CA 95134\n                   USA\n           E-mail: cs-erm@cisco.com')
if mibBuilder.loadTexts: ciscoErmCapability.setDescription('Agent capabilities for CISCO-ERM-MIB')
ciscoErmCapabilityV12R02SR = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 492, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErmCapabilityV12R02SR = ciscoErmCapabilityV12R02SR.setProductRelease('Cisco IOS 12.2SR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoErmCapabilityV12R02SR = ciscoErmCapabilityV12R02SR.setStatus('current')
if mibBuilder.loadTexts: ciscoErmCapabilityV12R02SR.setDescription('Cisco ERM Capabilities for IOS 12.2SR')
mibBuilder.exportSymbols("CISCO-ERM-CAPABILITY", ciscoErmCapability=ciscoErmCapability, PYSNMP_MODULE_ID=ciscoErmCapability, ciscoErmCapabilityV12R02SR=ciscoErmCapabilityV12R02SR)
