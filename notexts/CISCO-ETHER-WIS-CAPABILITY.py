#
# PySNMP MIB module CISCO-ETHER-WIS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ETHER-WIS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherWisCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 531))
ciscoEtherWisCapability.setRevisions(('2007-01-23 12:00',))
if mibBuilder.loadTexts: ciscoEtherWisCapability.setLastUpdated('200701231200Z')
if mibBuilder.loadTexts: ciscoEtherWisCapability.setOrganization('Cisco Systems, Inc.')
ciscoEtherWisCapabilityV120S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 531, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherWisCapabilityV120S = ciscoEtherWisCapabilityV120S.setProductRelease('Cisco IOS 12.0S for GSR.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherWisCapabilityV120S = ciscoEtherWisCapabilityV120S.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHER-WIS-CAPABILITY", ciscoEtherWisCapabilityV120S=ciscoEtherWisCapabilityV120S, PYSNMP_MODULE_ID=ciscoEtherWisCapability, ciscoEtherWisCapability=ciscoEtherWisCapability)
