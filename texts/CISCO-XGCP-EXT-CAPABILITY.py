#
# PySNMP MIB module CISCO-XGCP-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-XGCP-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoXgcpExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoXgcpExtCapability.setRevisions(('2004-06-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoXgcpExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setLastUpdated('200406180000Z')
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoXgcpExtCapability.setDescription('The capabilities description of\n                 CISCO-XGCP-EXT-MIB.')
ciscoXgcpExtCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpExtCapabilityV12R03 = ciscoXgcpExtCapabilityV12R03.setProductRelease('Cisco IOS 12.3.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoXgcpExtCapabilityV12R03 = ciscoXgcpExtCapabilityV12R03.setStatus('current')
if mibBuilder.loadTexts: ciscoXgcpExtCapabilityV12R03.setDescription('CISCO-XGCP-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-XGCP-EXT-CAPABILITY", ciscoXgcpExtCapability=ciscoXgcpExtCapability, ciscoXgcpExtCapabilityV12R03=ciscoXgcpExtCapabilityV12R03, PYSNMP_MODULE_ID=ciscoXgcpExtCapability)
