#
# PySNMP MIB module CISCO-SYSLOG-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYSLOG-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
ciscoSyslogExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 454))
ciscoSyslogExtCapability.setRevisions(('2008-06-30 00:00', '2006-04-18 00:00', '2005-09-01 00:00',))
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setLastUpdated('200806300000Z')
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSyslogExtCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityMDS3R0 = ciscoSyslogExtCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityMDS3R0 = ciscoSyslogExtCapabilityMDS3R0.setStatus('current')
ciscoSyslogExtCapabilityACSWV03R0000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityACSWV03R0000 = ciscoSyslogExtCapabilityACSWV03R0000.setProductRelease('ACSW (Application Control Software) 3.0\n                for Application Control Engine(ACE) module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityACSWV03R0000 = ciscoSyslogExtCapabilityACSWV03R0000.setStatus('obsolete')
ciscoSyslogExtCapACSWV03R0000Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapACSWV03R0000Rev1 = ciscoSyslogExtCapACSWV03R0000Rev1.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine(ACE) module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapACSWV03R0000Rev1 = ciscoSyslogExtCapACSWV03R0000Rev1.setStatus('current')
ciscoSyslogExtCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityc4710aceVA1R700 = ciscoSyslogExtCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityc4710aceVA1R700 = ciscoSyslogExtCapabilityc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSLOG-EXT-CAPABILITY", ciscoSyslogExtCapability=ciscoSyslogExtCapability, PYSNMP_MODULE_ID=ciscoSyslogExtCapability, ciscoSyslogExtCapabilityMDS3R0=ciscoSyslogExtCapabilityMDS3R0, ciscoSyslogExtCapACSWV03R0000Rev1=ciscoSyslogExtCapACSWV03R0000Rev1, ciscoSyslogExtCapabilityACSWV03R0000=ciscoSyslogExtCapabilityACSWV03R0000, ciscoSyslogExtCapabilityc4710aceVA1R700=ciscoSyslogExtCapabilityc4710aceVA1R700)
