#
# PySNMP MIB module CISCO-IETF-ISIS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-ISIS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
ciscoIetfIsisCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 446))
ciscoIetfIsisCapability.setRevisions(('2005-08-18 00:00',))
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setLastUpdated('200508180000Z')
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfIsisCapV12R0225SG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 446, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfIsisCapV12R0225SG = ciscoIetfIsisCapV12R0225SG.setProductRelease('Cisco IOS 12.2(25)SG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfIsisCapV12R0225SG = ciscoIetfIsisCapV12R0225SG.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-ISIS-CAPABILITY", ciscoIetfIsisCapability=ciscoIetfIsisCapability, PYSNMP_MODULE_ID=ciscoIetfIsisCapability, ciscoIetfIsisCapV12R0225SG=ciscoIetfIsisCapV12R0225SG)
