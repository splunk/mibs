#
# PySNMP MIB module SYSLOG-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SYSLOG-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, TimeTicks, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, mib_2, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "mib-2", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
syslogTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 173))
syslogTCMIB.setRevisions(('2009-03-30 00:00',))
if mibBuilder.loadTexts: syslogTCMIB.setLastUpdated('200903300000Z')
if mibBuilder.loadTexts: syslogTCMIB.setOrganization('IETF Syslog Working Group')
class SyslogFacility(TextualConvention, Integer32):
    reference = 'The Syslog Protocol (RFC5424): Table 1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kern", 0), ("user", 1), ("mail", 2), ("daemon", 3), ("auth", 4), ("syslog", 5), ("lpr", 6), ("news", 7), ("uucp", 8), ("cron", 9), ("authpriv", 10), ("ftp", 11), ("ntp", 12), ("audit", 13), ("console", 14), ("cron2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class SyslogSeverity(TextualConvention, Integer32):
    reference = 'The Syslog Protocol (RFC5424): Table 2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emerg", 0), ("alert", 1), ("crit", 2), ("err", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

mibBuilder.exportSymbols("SYSLOG-TC-MIB", SyslogFacility=SyslogFacility, syslogTCMIB=syslogTCMIB, PYSNMP_MODULE_ID=syslogTCMIB, SyslogSeverity=SyslogSeverity)
