#
# PySNMP MIB module CISCO-SYSAPPL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYSAPPL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
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
ciscoSysApplCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 999))
ciscoSysApplCapability.setRevisions(('2007-09-14 00:00',))
if mibBuilder.loadTexts: ciscoSysApplCapability.setLastUpdated('200709140000Z')
if mibBuilder.loadTexts: ciscoSysApplCapability.setOrganization('Cisco Systems, Inc.')
ciscoSysApplCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysApplCapabilityCTSV120 = ciscoSysApplCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.2.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysApplCapabilityCTSV120 = ciscoSysApplCapabilityCTSV120.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSAPPL-CAPABILITY", ciscoSysApplCapabilityCTSV120=ciscoSysApplCapabilityCTSV120, ciscoSysApplCapability=ciscoSysApplCapability, PYSNMP_MODULE_ID=ciscoSysApplCapability)
