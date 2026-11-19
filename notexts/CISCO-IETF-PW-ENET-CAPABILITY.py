#
# PySNMP MIB module CISCO-IETF-PW-ENET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-PW-ENET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfPwEnetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 428))
ciscoIetfPwEnetCapability.setRevisions(('2004-11-29 12:00',))
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setLastUpdated('200411291200Z')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setOrganization('Cisco Systems, Inc.')
ciscoIetfPwEnetCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 428, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setProductRelease('Cisco IOS 12.0(28)S, Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PW-ENET-CAPABILITY", ciscoIetfPwEnetCapability=ciscoIetfPwEnetCapability, PYSNMP_MODULE_ID=ciscoIetfPwEnetCapability, ciscoIetfPwEnetCapabilityV12R00=ciscoIetfPwEnetCapabilityV12R00)
